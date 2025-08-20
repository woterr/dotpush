import argparse
from . import main as m


def main():
    parser = argparse.ArgumentParser(
        description="A tool that helps backup dotfiles and automatically push to a remote github repository."
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    subparsers.required = True

    subparsers.add_parser("init", help="Initialize DotPush")
    subparsers.add_parser("backup", help="Backup dotfiles to local directory")
    # parser_init.add_argument(...)

    args = parser.parse_args()

    if args.command == "init":
        m.init()
    if args.command == "backup":
        m.backup()
