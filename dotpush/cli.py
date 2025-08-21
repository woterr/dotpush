import argparse
from . import main as m


def main():
    """
    This function handles argument parsing logic.
    """
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
