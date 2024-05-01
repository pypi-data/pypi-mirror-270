import asyncio
import os
import resemble.cli.terminal as terminal
import sys
from resemble.cli.cloud import cloud_down, cloud_up, register_cloud
from resemble.cli.dev import dev_expunge, dev_run, register_dev
from resemble.cli.protoc import protoc, register_protoc
from resemble.cli.rc import ArgumentParser
from resemble.cli.secret import register_secret, secret_delete, secret_write
from resemble.cli.subprocesses import Subprocesses
from typing import Optional


def create_parser(
    *,
    rc_file: Optional[str] = None,
    argv: Optional[list[str]] = None,
) -> ArgumentParser:
    parser = ArgumentParser(
        program='rsm',
        filename='.rsmrc',
        subcommands=[
            'dev run',
            'dev expunge',
            'protoc',
            'secret write',
            'secret delete',
            'cloud up',
            'cloud down',
        ],
        rc_file=rc_file,
        argv=argv,
    )

    register_dev(parser)
    register_protoc(parser)
    register_secret(parser)
    register_cloud(parser)

    return parser


async def rsm():
    # Sets up the terminal for logging.
    verbose, argv = ArgumentParser.strip_any_arg(sys.argv, '-v', '--verbose')
    terminal.init(verbose=verbose)

    # Install signal handlers to help ensure that Subprocesses get cleaned up.
    Subprocesses.install_terminal_app_signal_handlers()

    parser = create_parser(argv=argv)

    args, argv_after_dash_dash = parser.parse_args()

    if args.subcommand == 'dev run':
        return await dev_run(args, parser=parser)
    elif args.subcommand == 'dev expunge':
        return await dev_expunge(args)
    elif args.subcommand == 'protoc':
        return await protoc(args, argv_after_dash_dash, parser=parser)
    elif args.subcommand == 'secret write':
        return await secret_write(args)
    elif args.subcommand == 'secret delete':
        return await secret_delete(args)
    elif args.subcommand == 'cloud up':
        return await cloud_up(args)
    elif args.subcommand == 'cloud down':
        return await cloud_down(args)

    raise NotImplementedError(
        f"Subcommand '{args.subcommand}' is not implemented"
    )


# This is a separate function (rather than just being in `__main__`) so that we
# can refer to it as a `script` in our `pyproject.rsm.toml` file.
def main():
    # We ignore _known_ warnings from
    # `multiprocessing.resource_tracker` that we know are harmless so
    # that we don't spam stdout. See #2793.
    #
    # We do this via an environment variable instead of using
    # `warnings.filterwarnings()` because we fork/exec multiple
    # processes and need to make sure all of those processes ignore
    # these warnings.
    warnings = os.environ.get('PYTHONWARNINGS')
    if warnings is not None:
        warnings += ','
    else:
        warnings = ''

    warnings += (
        'ignore:resource_tracker:UserWarning:multiprocessing.resource_tracker'
    )

    os.environ['PYTHONWARNINGS'] = warnings

    try:
        returncode = asyncio.run(rsm())
        sys.exit(returncode)
    except KeyboardInterrupt:
        # Don't print an exception and stack trace if the user does a
        # Ctrl-C.
        pass


if __name__ == '__main__':
    main()
