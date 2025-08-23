import argparse
import sys
from . import main as m
from .utils import timer


def main():
    """
    This function handles argument parsing logic.
    """
    is_interactive = sys.stdout.isatty()

    command = sys.argv[1] if len(sys.argv) else None

    if is_interactive and command and command != "init":
        if not timer.is_timer_active():
            try:
                prompt = input(
                    "? Automatic hourly backups are not enabled. Would you like to enable them now? [y/N]:"
                )
                if prompt.lower().strip() in ["y", "yes", ""]:
                    timer.enable_timer()
                else:
                    print(
                        "-> You can enable the timer later by running: systemctl --user enable --now dotpush.timer"
                    )
            except (KeyboardInterrupt, EOFError):
                print("\n-> Setup cancelled.")

    parser = argparse.ArgumentParser(
        description="A tool that helps backup dotfiles and automatically push to a remote github repository."
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    subparsers.required = True

    parser_init = subparsers.add_parser("init", help="Initialize DotPush")
    parser_init.add_argument(
        "service",
        nargs="?",
        choices=["github"],
        default=None,
        help="Optional: Specify 'github' to initialize with GitHub integration.",
    )
    subparsers.add_parser("backup", help="Backup dotfiles to local directory")
    subparsers.add_parser("push", help="Push DotFiles to a github repository")

    args = parser.parse_args()

    if args.command == "init":
        m.init(service=args.service)
    if args.command == "backup":
        m.backup()
    if args.command == "push":
        m.push()
