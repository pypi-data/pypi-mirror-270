import aiofiles.os
import asyncio
import grpc
import os
import random
import shutil
import sys
import termios
import tty
from colorama import Fore
from contextlib import asynccontextmanager
from grpc_health.v1 import health_pb2, health_pb2_grpc
from pathlib import Path
from resemble.aio.contexts import EffectValidation
# We import the whole `terminal` module (as opposed to the methods it contains)
# to allow us to mock these methods out in tests.
from resemble.cli import terminal
from resemble.cli.cloud import add_cloud_options
from resemble.cli.directories import (
    add_working_directory_options,
    dot_rsm_dev_directory,
    use_working_directory,
)
from resemble.cli.monkeys import monkeys, no_chaos_monkeys
# We won't mock the classes in `rc`, so it's safe to import those directly.
from resemble.cli.rc import ArgumentParser, BaseTransformer, TransformerError
from resemble.cli.subprocesses import Subprocesses
from resemble.cli.watch import watch
from resemble.settings import (
    DEFAULT_SECURE_PORT,
    DOCS_BASE_URL,
    ENVOY_PROXY_IMAGE,
    ENVVAR_RSM_CLOUD_API_KEY,
    ENVVAR_RSM_CLOUD_GATEWAY_ADDRESS,
    ENVVAR_RSM_CLOUD_GATEWAY_SECURE_CHANNEL,
    ENVVAR_RSM_DEV,
    ENVVAR_RSM_DEV_EFFECT_VALIDATION,
    ENVVAR_RSM_DEV_INSPECT_PORT,
    ENVVAR_RSM_DEV_LOCAL_ENVOY,
    ENVVAR_RSM_DEV_LOCAL_ENVOY_PORT,
    ENVVAR_RSM_DEV_NAME,
    ENVVAR_RSM_DEV_SECRETS_DIRECTORY,
    ENVVAR_RSM_DOT_RSM_DEV_DIRECTORY,
    SIDECAR_SUFFIX,
)
from typing import Any, Optional


class EnvTransformer(BaseTransformer):

    def transform(self, value: str):
        if '=' not in value:
            raise TransformerError(
                f"Invalid flag '--env={value}': must be in the form "
                "'--env=KEY=VALUE'"
            )
        return value.split('=', 1)


def register_dev(parser: ArgumentParser):
    _register_dev_run(parser)
    _register_dev_expunge(parser)


def _register_dev_run(parser: ArgumentParser):
    add_working_directory_options(parser.subcommand('dev run'))

    parser.subcommand('dev run').add_argument(
        '--name',
        type=str,
        help="name of application; state will be persisted using this name in "
        f"'{dot_rsm_dev_directory()}'",
    )

    parser.subcommand('dev run').add_argument(
        '--background-command',
        type=str,
        repeatable=True,
        help=
        'command(s) to execute in the background (multiple instances of this '
        'flag are supported)',
    )

    parser.subcommand('dev run').add_argument(
        '--local-envoy',
        type=bool,
        default=True,
        help='whether or not to bring up a local Envoy'
    )

    parser.subcommand('dev run').add_argument(
        '--local-envoy-port',
        type=int,
        help=f'port for local Envoy; defaults to {DEFAULT_LOCAL_ENVOY_PORT}',
    )

    parser.subcommand('dev run').add_argument(
        '--inspect-port',
        type=int,
        help=f'port for inspecting state; defaults to {DEFAULT_INSPECT_PORT}',
    )

    parser.subcommand('dev run').add_argument(
        '--python',
        type=bool,
        default=False,
        help="whether or not to launch the application by "
        "passing it as an argument to 'python'",
    )

    parser.subcommand('dev run').add_argument(
        '--watch',
        type=str,
        repeatable=True,
        help=
        'path to watch; multiple instances are allowed; globbing is supported',
    )

    parser.subcommand('dev run').add_argument(
        '--chaos',
        type=bool,
        default=True,
        help='whether or not to randomly induce failures',
    )

    parser.subcommand('dev run').add_argument(
        '--effect-validation',
        type=str,
        default="quiet",
        help=(
            'Whether to validate effects in development mode. '
            f'See {DOCS_BASE_URL}/docs/model/side_effects for more '
            'information.'
        ),
    )

    parser.subcommand('dev run').add_argument(
        "--env",
        type=str,
        repeatable=True,
        transformer=EnvTransformer(),
        help=
        "sets any specified environment variables before running the application; "
        "'ENV' should be of the form 'KEY=VALUE'",
    )

    parser.subcommand('dev run').add_argument(
        "--protoc-watch",
        type=bool,
        default=True,
        help="also run `rsm protoc --watch` in the background if true, taking "
        "'protoc' arguments from the '.rsmrc' file, which must be present"
    )

    parser.subcommand('dev run').add_argument(
        'application',
        type=str,  # TODO: consider argparse.FileType('e')
        help='path to application to execute',
    )

    parser.subcommand('dev run').add_argument(
        "--secrets-directory",
        type=Path,
        default=None,
        help=(
            "A directory to use to override the default source of Secrets. "
            "By default, Secrets are read from the Resemble Cloud API, and are written using "
            "`rsm secret write`."
        )
    )

    # The `dev` command does not require an API key, since not everyone will
    # have access to secrets on day one.
    add_cloud_options(parser.subcommand('dev run'), api_key_required=False)


def _register_dev_expunge(parser: ArgumentParser):
    parser.subcommand('dev expunge').add_argument(
        '--name',
        type=str,
        help="name of the application to expunge; will remove this "
        f"application's state from '{dot_rsm_dev_directory()}'",
        required=True,
    )


async def _run_background_command(
    background_command: str,
    *,
    verbose: bool,
    print_as: Optional[str] = None,
    subprocesses: Subprocesses,
):
    # TODO: Align this with the global `terminal.is_verbose` boolean. We always
    # want error output in case of failure, but we might only want streamed output
    # if `is_verbose`.
    if verbose:
        terminal.info(
            f"Running background command '{print_as or background_command}'"
        )

    async with subprocesses.shell(background_command) as process:
        await process.wait()

        if process.returncode != 0:
            terminal.fail(
                f"Failed to run background command '{background_command}', "
                f"exited with {process.returncode}"
            )
        elif verbose:
            terminal.warn(
                f"Background command '{background_command}' exited without errors"
            )


@asynccontextmanager
async def _run(
    application,
    *,
    env: dict[str, str],
    launcher: Optional[str],
    subprocesses: Subprocesses,
):
    """Helper for running the application with an optional launcher."""
    args = [application] if launcher is None else [launcher, application]

    async with subprocesses.exec(*args, env=env) as process:
        yield process


async def _check_docker_status(subprocesses: Subprocesses):
    """Checks if Docker is running and can use the Envoy proxy image. Downloads
    that image if necessary."""
    async with subprocesses.exec(
        'docker',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    ) as process:
        stdout, _ = await process.communicate()
        if process.returncode != 0:
            terminal.fail(
                f"Could not use Docker:\n"
                "\n"
                f"{stdout.decode() if stdout is not None else '<no output>'}"
            )

    # The '-q' flag returns only the image ID, so if stdout is empty
    # then the image is not downloaded.
    async with subprocesses.exec(
        'docker',
        'images',
        '-q',
        ENVOY_PROXY_IMAGE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    ) as process:
        stdout, _ = await process.communicate()

        if process.returncode != 0:
            terminal.fail(
                f"Could not use Docker; 'docker images -q {ENVOY_PROXY_IMAGE}' failed with output:\n"
                "\n"
                f"{stdout.decode() if stdout is not None else '<no output>'}"
            )
        elif stdout is None or stdout == b'':
            # Empty output means the image is not downloaded because
            # 'docker' didn't find a match for the image name.
            terminal.info(
                f"Pulling Envoy proxy image '{ENVOY_PROXY_IMAGE}'..."
            )
            async with subprocesses.exec(
                'docker',
                'pull',
                ENVOY_PROXY_IMAGE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT,
            ) as process:
                stdout, _ = await process.communicate()
                if process.returncode != 0:
                    terminal.fail(
                        f"Could not use Docker; 'docker pull {ENVOY_PROXY_IMAGE}' failed with output:\n"
                        "\n"
                        f"{stdout.decode() if stdout is not None else '<no output>'}"
                    )


async def _check_local_envoy_status(port: int):
    """Checks if the application is up and running."""
    # Using 'dev' subdomain of 'localhost.direct' as a workaround on a
    # gRPC bug that produces log message error about not matching the
    # entry (*.localhost.direct) in the certificate.  See
    # https://github.com/reboot-dev/respect/issues/2305
    #
    # We also want to print out 'dev.localhost.direct' so that our
    # users copy that to also avoid getting the log message error from
    # their gRPC or Resemble calls.
    address = f'dev.localhost.direct:{port}'

    last_status: bool = False
    while True:
        try:
            async with grpc.aio.secure_channel(
                address,
                grpc.ssl_channel_credentials(),
            ) as channel:
                response = await health_pb2_grpc.HealthStub(channel).Check(
                    health_pb2.HealthCheckRequest()
                )

                current_status = (
                    response.status == health_pb2.HealthCheckResponse.SERVING
                )
        except grpc.aio.AioRpcError:
            current_status = False

        if current_status != last_status:
            last_status = current_status

            if current_status:
                terminal.info("Application is serving traffic ...\n")
                terminal.info(
                    f"  Your API is available at https://{address}\n"
                    "\n"
                    f"  You can use {address} as the `gateway` for a `Workflow`\n"
                    "\n"
                    "  You can inspect your state at http://localhost:9992\n",
                    color=Fore.WHITE,
                )
            else:
                terminal.warn("Application stopped serving traffic\n")

        await asyncio.sleep(.5)


async def _cancel_all(tasks: list[asyncio.Task]) -> None:
    if not tasks:
        return

    for task in tasks:
        task.cancel()

    await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)


def use_protoc_watch(args, parser: ArgumentParser) -> bool:
    """Check whether we can run `rsm protoc --watch` without further
    user-specified arguments. That depends on whether the user has
    specified the necessary arguments (notably `--output-directory`)
    in an `.rsmrc`."""
    if args.protoc_watch:
        if parser.dot_rc is None:
            terminal.fail(
                "The '--protoc-watch' flag was specified, but no '.rsmrc' file was found. "
                "Add an '.rsmrc' file containing the necessary arguments to run 'rsm protoc' "
                "to use 'rsm dev run --protoc-watch'"
            )
        return True
    return False


async def induce_chaos() -> Optional[int]:
    """Helper that allows inducing chaos via pressing keys 0-9."""

    def read(future: asyncio.Future[Optional[int]]):
        value = sys.stdin.read(1)
        if value == '0':
            # No delay, restart app immediately.
            future.set_result(None)
        elif value in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # Delay restarting app by the 2 raised to the power of the
            # key pressed, e.g., if '3' was pressed we'll wait 8
            # seconds, if '4' is pressed we'll wait 16 seconds, if '9'
            # was pressed we'll wait 512 seconds (almost 10 minutes).
            future.set_result(2**int(value))

    future: asyncio.Future[Optional[int]] = asyncio.Future()

    # Add an async file descriptor reader to our running event
    # loop so that we know when a key has been pressed.
    loop = asyncio.get_running_loop()

    sys_stdin_fd = sys.stdin.fileno()

    loop.add_reader(sys_stdin_fd, read, future)

    try:
        return await future
    finally:
        loop.remove_reader(sys_stdin_fd)


DEFAULT_LOCAL_ENVOY_PORT: int = DEFAULT_SECURE_PORT
DEFAULT_INSPECT_PORT: int = 9992


async def dev_run(args, *, parser: ArgumentParser):
    """Implementation of the 'dev run' subcommand."""

    if parser.dot_rc is not None:
        while True:
            async with watch([parser.dot_rc]) as rc_file_event_task:
                await _inner_dev_run(
                    args, parser=parser, rc_file_event_task=rc_file_event_task
                )
            args, _ = parser.parse_args()
    else:
        await _inner_dev_run(args, parser=parser, rc_file_event_task=None)


async def _inner_dev_run(
    args,
    *,
    parser: ArgumentParser,
    rc_file_event_task: Optional[asyncio.Task] = None
) -> None:
    """Runs until the given rc_file_event_task triggers, or an exception is raised."""

    # Determine the working directory and move into it.
    with use_working_directory(args, parser, verbose=True):
        application = os.path.abspath(args.application)

        # Use `Subprocesses` to manage all of our subprocesses for us.
        subprocesses = Subprocesses()

        # If on Linux try and become a child subreaper so that we can
        # properly clean up all processes descendant from us!
        if sys.platform == 'linux':
            # The 'pyprctl' module is available on Linux only.
            import pyprctl
            try:
                pyprctl.set_child_subreaper(True)
            except:
                terminal.warn(
                    "Failed to become child subreaper, we'll do our "
                    "best to ensure all created processes are terminated"
                )
                pass

        # Run any background commands.
        background_command_tasks: list[asyncio.Task] = []

        for background_command in args.background_command or []:
            background_command_tasks.append(
                asyncio.create_task(
                    _run_background_command(
                        background_command,
                        verbose=True,
                        subprocesses=subprocesses,
                    )
                )
            )

        if use_protoc_watch(args, parser):
            # Run `rsm protoc` _once_, so that the application doesn't
            # exit because it can't find any of the generated files.
            #
            # TODO(rjh,gorm): the downside of this is that we _only_ guarantee
            #                 that proto changes have been seen at start-time.
            #                 Ideally, we'd instead have a more general state
            #                 machine that goes:
            #                 1. Run protoc.
            #                 2. Start application.
            #                 3. Wait for application code OR proto files to
            #                    change.
            #                 4. Stop application.
            #                 5. If proto files changed, go back to 1. Else go
            #                    back to 2.
            #
            # Using `sys.argv[0]` in the event that `rsm` is
            # not on the path or someone renamed it.
            #
            # TODO(benh): aggregate all of the `--config=` and pass
            # them on to `rsm protoc`.
            rsm_protoc = f'{sys.executable} {sys.argv[0]} protoc'
            async with subprocesses.shell(
                rsm_protoc,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT,
            ) as process:
                stdout, _ = await process.communicate()

                if process.returncode != 0:
                    terminal.fail(
                        "Failed to run 'rsm protoc' (you can disable this with --no-protoc-watch):\n"
                        "\n"
                        f"{stdout.decode() if stdout is not None else '<no output>'}"
                    )

            background_command_tasks.append(
                asyncio.create_task(
                    _run_background_command(
                        # We do not currently pass '--verbose' to
                        # protoc, as we don't want the `protoc`
                        # generation itself to be verbose, but we
                        # might want to change that once '--verbose'
                        # can be passed to 'rsm dev'.
                        #
                        # We pass 'verbose=False' to
                        # `_run_background_command` because we don't
                        # need it to tell us it is running it in the
                        # background.
                        #
                        # We need to pass '--wait-for-changes' to
                        # not immediately run 'rsm protoc' again. It will
                        # modify the source files and restart the app.
                        # See more https://github.com/reboot-dev/respect/issues/2898
                        f'{rsm_protoc} --watch --wait-for-changes',
                        verbose=False,
                        print_as='rsm protoc --watch --wait-for-changes',
                        subprocesses=subprocesses,
                    )
                )
            )

        # Set all the environment variables that
        # 'resemble.aio.Application' will be looking for.
        #
        # We make a copy of the environment so that we don't change
        # our environment variables which might cause an issue.
        env = os.environ.copy()

        env[ENVVAR_RSM_DEV] = 'true'

        if args.name is not None:
            env[ENVVAR_RSM_DEV_NAME] = args.name
            env[ENVVAR_RSM_DOT_RSM_DEV_DIRECTORY] = dot_rsm_dev_directory()

        if args.secrets_directory is not None:
            env[ENVVAR_RSM_DEV_SECRETS_DIRECTORY] = args.secrets_directory

        if args.local_envoy:
            # Check if Docker is running and can access the Envoy proxy image.
            # Fail otherwise.
            await _check_docker_status(subprocesses)
            env[ENVVAR_RSM_DEV_LOCAL_ENVOY] = 'true'

            background_command_tasks.append(
                asyncio.create_task(
                    _check_local_envoy_status(
                        args.local_envoy_port or DEFAULT_LOCAL_ENVOY_PORT
                    )
                )
            )

        else:
            env[ENVVAR_RSM_DEV_LOCAL_ENVOY] = 'false'

        env[ENVVAR_RSM_DEV_LOCAL_ENVOY_PORT] = str(
            args.local_envoy_port or DEFAULT_LOCAL_ENVOY_PORT
        )

        try:
            # TODO: In Python 3.12, can use `choice in Enum`.
            EffectValidation[args.effect_validation.upper()]
        except KeyError:
            options = ', '.join(e.name.lower() for e in EffectValidation)
            terminal.fail(
                f"Unexpected value for --effect-validation: `{args.effect_validation}`. "
                f"Legal values are: {options}"
            )
        env[ENVVAR_RSM_DEV_EFFECT_VALIDATION] = args.effect_validation.upper()

        env[ENVVAR_RSM_DEV_INSPECT_PORT] = str(
            args.inspect_port or DEFAULT_INSPECT_PORT
        )

        if args.api_key is not None:
            env[ENVVAR_RSM_CLOUD_API_KEY] = args.api_key
        env[ENVVAR_RSM_CLOUD_GATEWAY_ADDRESS] = args.cloud_cell_address
        env[ENVVAR_RSM_CLOUD_GATEWAY_SECURE_CHANNEL
           ] = 'true' if args.cloud_secure_channel else 'false'

        # Also include all environment variables from '--env='.
        for (key, value) in args.env or []:
            env[key] = value

        if not args.chaos:
            terminal.warn(
                '\n' + random.choice(no_chaos_monkeys) + '\n'
                'You Have Disabled Chaos Monkey! (see --chaos)\n'
                '\n'
                'Only You (And Chaos Monkey) Can Prevent Bugs!'
                '\n'
            )

        # Bool used to steer the printing. i.e., are we starting or restarting
        # the application?
        first_start = True

        # Optional delay, used for inducing chaos with a delay.
        delay: Optional[int] = None

        # Save the old tty settings so we can set them back to that
        # when exiting.
        sys_stdin_fd = sys.stdin.fileno()

        old_tty_settings: Optional[Any] = None

        # In some environments, e.g., CI, we don't have a tty, nor do
        # we need one as we're not expecting to read from stdin.
        if sys.stdin.isatty():
            old_tty_settings = termios.tcgetattr(sys_stdin_fd)

            # Set the tty to not echo key strokes back to the terminal
            # and also remove buffering so we can read a single key
            # stroke at a time (yes, `tty.setcbreak()` does all that!)
            tty.setcbreak(sys_stdin_fd)

        try:
            while True:
                if delay is not None:
                    await asyncio.sleep(delay)
                    delay = None

                # Clear the screen as we (re)start the application.
                os.system('clear')

                # Determine the appropriate verb.
                start_verb = "Starting" if first_start else "Restarting"
                if args.name is None:
                    terminal.warn(
                        f'{start_verb} an ANONYMOUS application; to reuse state '
                        'across application restarts use --name'
                        '\n'
                    )
                else:
                    terminal.info(
                        f'{start_verb} application with name "{args.name}"...'
                        '\n'
                    )
                first_start = False

                # It's possible that the application may get deleted
                # and then (re)created by a build system so rather
                # than fail if we can't find it we'll retry but print
                # out a warning every ~10 seconds (which corresponds
                # to ~20 retries since we sleep for 0.5 seconds
                # between each retry).
                retries = 0
                while not await aiofiles.os.path.isfile(application):
                    if retries != 0 and retries % 20 == 0:
                        terminal.warn(
                            f"Missing application at '{application}' "
                            "(is it being rebuilt?)"
                        )
                    retries += 1
                    await asyncio.sleep(0.5)

                # Expect an executable if we haven't been asked to use
                # `python`.
                if (
                    args.python is None and
                    not await aiofiles.os.access(application, os.X_OK)
                ):
                    terminal.fail(
                        f"Expecting executable application at '{application}'. "
                        "Specify '--python' if you want to run a Python application."
                    )

                async with watch(
                    [application] + (args.watch or [])
                ) as file_system_event_task:
                    # TODO(benh): catch just failure to create the subprocess
                    # so that we can either try again or just listen for a
                    # modified event and then try again.
                    async with _run(
                        application,
                        env=env,
                        launcher=sys.executable
                        if args.python is not None else None,
                        subprocesses=subprocesses,
                    ) as process:
                        process_wait_task = asyncio.create_task(process.wait())

                        induce_chaos_task = asyncio.create_task(induce_chaos())

                        chaos_task: Optional[asyncio.Task] = None
                        if args.chaos:
                            chaos_task = asyncio.create_task(
                                asyncio.sleep(600)
                            )

                        completed, pending = await asyncio.wait(
                            [
                                file_system_event_task,
                                process_wait_task,
                                induce_chaos_task,
                                *([chaos_task] if chaos_task else []),
                                *(
                                    [rc_file_event_task]
                                    if rc_file_event_task else []
                                ),
                            ],
                            return_when=asyncio.FIRST_COMPLETED,
                        )

                        # Cancel tasks regardless of what completed
                        # first as we won't ever wait on them.
                        induce_chaos_task.cancel()

                        if chaos_task:
                            chaos_task.cancel()

                        task = completed.pop()

                        if task is process_wait_task:
                            terminal.warn(
                                '\n'
                                'Application exited unexpectedly '
                                f'(with code {process_wait_task.result()}) '
                                '... waiting for modification'
                                '\n'
                            )
                            # NOTE: we'll wait for a file system event
                            # below to signal a modification!
                        elif (
                            (task is induce_chaos_task) or
                            (args.chaos and task is chaos_task)
                        ):
                            terminal.warn(
                                '\n'
                                'Chaos Monkey Is Restarting Your Application'
                                '\n' + random.choice(monkeys) + '\n'
                                '... disable via --no-chaos if you must'
                                '\n'
                                '\n'
                            )
                            if task is induce_chaos_task:
                                delay = await task
                            continue
                        elif task is rc_file_event_task:
                            terminal.info(
                                '\n'
                                f'{parser.dot_rc_filename} modified; restarting ... '
                                '\n'
                            )
                            await _cancel_all(background_command_tasks)
                            return

                        await file_system_event_task

                        terminal.info(
                            '\n'
                            'Application modified; restarting ... '
                            '\n'
                        )
        except:
            await _cancel_all(background_command_tasks)
            raise
        finally:
            # Reset the terminal to old settings, i.e., make key
            # strokes be echoed, etc.
            if old_tty_settings is not None:
                termios.tcsetattr(
                    sys_stdin_fd, termios.TCSADRAIN, old_tty_settings
                )


async def dev_expunge(args):
    """
    Delete the sidecar state directory for the application with the given name.
    """
    application_directory = (
        Path(dot_rsm_dev_directory()) / (args.name + SIDECAR_SUFFIX)
    )
    try:
        shutil.rmtree(application_directory)
        terminal.info(f"Application '{args.name}' has been expunged")
    except FileNotFoundError:
        terminal.fail(
            f"Could not find application with name '{args.name}' (looked in "
            f"'{application_directory}'); did not expunge"
        )
