"""
Simple folder synchronization using FTP.

(c) 2012-2024 Martin Wendt; see https://github.com/mar10/pyftpsync
Licensed under the MIT license: https://www.opensource.org/licenses/mit-license.php

Usage examples:
  > pyftpsync.py --help
  > pyftpsync.py upload . ftps://example.com/myfolder
"""

import argparse
import platform
import sys
from pprint import pprint

from ftpsync import __version__
from ftpsync.cli_common import (
    common_parser,
    creds_parser,
    matcher_parser,
    verbose_parser,
)
from ftpsync.run_command import add_run_parser, handle_run_command
from ftpsync.scan_command import add_scan_parser
from ftpsync.synchronizers import (
    BiDirSynchronizer,
    DownloadSynchronizer,
    UploadSynchronizer,
)
from ftpsync.targets import FsTarget, make_target
from ftpsync.tree_command import add_tree_parser
from ftpsync.util import (
    DEBUG_FLAGS,
    PYTHON_VERSION,
    CliSilentRuntimeError,
    check_cli_verbose,
    namespace_to_dict,
    set_pyftpsync_logger,
)


# ===============================================================================
# run
# ===============================================================================
def run():
    """CLI main entry point."""

    # Use print() instead of logging when running in CLI mode:
    set_pyftpsync_logger(None)

    parser = argparse.ArgumentParser(
        description="Synchronize folders over FTP.",
        epilog="See also https://github.com/mar10/pyftpsync",
        parents=[verbose_parser],
        allow_abbrev=False,
    )

    # Note: we want to allow --version to be combined with --verbose. However
    # on Py2, argparse makes sub-commands mandatory, unless `action="version"` is used.
    if check_cli_verbose(3) > 3:
        version_info = "pyftpsync/{} Python/{} {}".format(
            __version__, PYTHON_VERSION, platform.platform()
        )
        version_info += f", Python: {sys.executable}"
    else:
        version_info = f"{__version__}"

    parser.add_argument("-V", "--version", action="version", version=version_info)

    subparsers = parser.add_subparsers(help="sub-command help")

    # --- Create the parser for the "upload" command ---------------------------

    sp = subparsers.add_parser(
        "upload",
        parents=[verbose_parser, common_parser, matcher_parser, creds_parser],
        help="copy new and modified files to remote folder",
        allow_abbrev=False,
    )

    sp.add_argument(
        "local",
        metavar="LOCAL",
        default=".",
        help="path to local folder (default: %(default)s)",
    )
    sp.add_argument("remote", metavar="REMOTE", help="path to remote folder")
    sp.add_argument(
        "--force",
        action="store_true",
        help="overwrite remote files, even if the target is newer "
        "(but no conflict was detected)",
    )
    sp.add_argument(
        "--resolve",
        default="ask",
        choices=["local", "skip", "ask"],
        help="conflict resolving strategy (default: '%(default)s')",
    )
    sp.add_argument(
        "--delete",
        action="store_true",
        help="remove remote files if they don't exist locally",
    )
    sp.add_argument(
        "--delete-unmatched",
        action="store_true",
        help="remove remote files if they don't exist locally "
        "or don't match the current filter (implies '--delete' option)",
    )
    sp.add_argument(
        "--create-folder",
        action="store_true",
        help="create remote folder if missing",
    )
    sp.add_argument(
        "--report-problems",
        action="store_true",
        help="return exit code 10 if any conflict was skipped, a copy error occurred, etc.",
    )

    sp.set_defaults(command="upload")

    # --- Create the parser for the "download" command -------------------------

    sp = subparsers.add_parser(
        "download",
        parents=[verbose_parser, common_parser, matcher_parser, creds_parser],
        help="copy new and modified files from remote folder to local target",
        allow_abbrev=False,
    )

    sp.add_argument(
        "local",
        metavar="LOCAL",
        default=".",
        help="path to local folder (default: %(default)s)",
    )
    sp.add_argument("remote", metavar="REMOTE", help="path to remote folder")
    sp.add_argument(
        "--force",
        action="store_true",
        help="overwrite local files, even if the target is newer "
        "(but no conflict was detected)",
    )
    sp.add_argument(
        "--resolve",
        default="ask",
        choices=["remote", "skip", "ask"],
        help="conflict resolving strategy (default: '%(default)s')",
    )
    sp.add_argument(
        "--delete",
        action="store_true",
        help="remove local files if they don't exist on remote target",
    )
    sp.add_argument(
        "--delete-unmatched",
        action="store_true",
        help="remove local files if they don't exist on remote target "
        "or don't match the current filter (implies '--delete' option)",
    )
    sp.add_argument(
        "--report-problems",
        action="store_true",
        help="return exit code 10 if any conflict was skipped, a copy error occurred, etc.",
    )

    sp.set_defaults(command="download")

    # --- Create the parser for the "sync" command -----------------------------

    sp = subparsers.add_parser(
        "sync",
        parents=[verbose_parser, common_parser, matcher_parser, creds_parser],
        help="synchronize new and modified files between remote folder and local target",
        allow_abbrev=False,
    )

    sp.add_argument(
        "local",
        metavar="LOCAL",
        default=".",
        help="path to local folder (default: %(default)s)",
    )
    sp.add_argument("remote", metavar="REMOTE", help="path to remote folder")
    sp.add_argument(
        "--resolve",
        default="ask",
        choices=["old", "new", "local", "remote", "skip", "ask"],
        help="conflict resolving strategy (default: '%(default)s')",
    )
    sp.add_argument(
        "--create-folder",
        action="store_true",
        help="create remote folder if missing",
    )
    sp.add_argument(
        "--report-problems",
        action="store_true",
        help="return exit code 10 if any conflict was skipped, a copy error occurred, etc.",
    )

    sp.set_defaults(command="sync")

    # --- Create the parser for the "run" command -----------------------------

    add_run_parser(subparsers)

    # --- Create the parser for the "scan" command -----------------------------

    add_scan_parser(subparsers)

    # --- Create the parser for the "tree" command -----------------------------

    add_tree_parser(subparsers)

    # --- Parse command line ---------------------------------------------------

    args = parser.parse_args()

    args.verbose -= args.quiet
    del args.quiet

    # print("verbose", args.verbose)

    ftp_debug = 0
    if args.verbose >= 6:
        ftp_debug = 1

    if args.debug:
        if args.verbose < 4:
            parser.error("'--debug' requires verbose level >= 4")
        DEBUG_FLAGS.update(args.debug)

    # --- Modify the `args` from the `pyftpsync.yaml` config -------------------

    if getattr(args, "command", None) == "run":
        handle_run_command(parser, args)

    # --- Handle `scan` and `tree` commands ------------------------------------

    if callable(getattr(args, "command", None)):
        try:
            return args.command(parser, args)
        except CliSilentRuntimeError as e:
            # This exception suppresses stacktrace in non-verbose mode
            print(f"\nERROR:\n{e}\n", file=sys.stderr)
            if args.verbose <= e.min_verbosity:
                sys.exit(e.exit_code)
            raise
        except KeyboardInterrupt:
            print("\nAborted by user.", file=sys.stderr)
            sys.exit(3)

    elif not hasattr(args, "command"):
        parser.error(
            "missing command (choose from 'upload', 'download', 'run', 'sync', 'scan', 'tree')"
        )

    # --- Post-process and check arguments -------------------------------------

    if hasattr(args, "delete_unmatched") and args.delete_unmatched:
        args.delete = True

    args.local_target = make_target(args.local, {"ftp_debug": ftp_debug})

    if args.remote == ".":
        parser.error("'.' is expected to be the local target (not remote)")

    args.remote_target = make_target(args.remote, {"ftp_debug": ftp_debug})
    if not isinstance(args.local_target, FsTarget) and isinstance(
        args.remote_target, FsTarget
    ):
        parser.error("a file system target is expected to be local")

    # --- Handle `upload`, `download`, and `sync` ------------------------------

    opts = namespace_to_dict(args)

    if args.command == "upload":
        s = UploadSynchronizer(args.local_target, args.remote_target, opts)
    elif args.command == "download":
        s = DownloadSynchronizer(args.local_target, args.remote_target, opts)
    elif args.command == "sync":
        s = BiDirSynchronizer(args.local_target, args.remote_target, opts)
    else:
        parser.error(f"unknown command '{args.command}'")

    # Allow prompting
    s.is_script = True

    try:
        s.run()
    except CliSilentRuntimeError as e:
        # This exception suppresses stacktrace in non-verbose mode
        print(f"\nERROR:\n{e}\n", file=sys.stderr)
        if args.verbose <= e.min_verbosity:
            sys.exit(e.exit_code)
        raise
    except KeyboardInterrupt:
        print("\nAborted by user.", file=sys.stderr)
        sys.exit(3)
    finally:
        # Prevent sporadic exceptions in ftplib, when closing in __del__
        s.local.close()
        s.remote.close()

    # --- Report results -------------------------------------------------------

    stats = s.get_stats()

    if args.verbose >= 5:
        pprint(stats)
    elif args.verbose >= 1:
        if args.dry_run:
            print("(DRY-RUN) ", end="")

        print(
            "Wrote {}/{} files in {} directories, skipped: {}, errors: {}.".format(
                stats["files_written"],
                stats["local_files"],
                stats["local_dirs"],
                stats["conflict_files_skipped"],  # + stats["copy_errors"],
                stats["errors"],
            ),
            end="",
        )
        if stats["interactive_ask"]:
            # Do not show timings when user prompts have been displayed
            print()
        else:
            print(" Elap: {}.".format(stats["elap_str"]))

    if getattr(args, "report_problems", None) and (
        s.problem_count() + s.error_count() > 0
    ):
        sys.exit(10)
    return


# Script entry point
if __name__ == "__main__":
    # Just in case...
    from multiprocessing import freeze_support

    freeze_support()

    run()
