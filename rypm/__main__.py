#! /usr/bin/env python3

"""
rypm - Ryuuzaki Ryuusei Plugin Manager

Usage:
    rypm <command> [<args>...]

Commands:
    install, add               Install a plugin
    uninstall, remove, rm      Uninstall a plugin
    update, upgrade, up        Update a plugin
    list, ls                   List installed plugins
    init                       Initialize `rypm` to be used remotely from the bot
    help                       Show this help message
"""
import argparse
import sys

import asyncio

python_version = sys.version_info
if python_version < (3, 10):
    print("rypm requires Python 3.10 or higher.")
    sys.exit(1)


__version__ = "0.0.1"


async def init():
    """Initialize `rypm` to be used remotely from the bot."""
    from rypm.init_hook import initialize as hook
    await hook()


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        prog="rypm",
        description="Ryuuzaki Ryuusei Plugin Manager",
        epilog="For more information, visit https://github.com/ryuuRyuusei/rypm",
        exit_on_error=True)
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "install", aliases=["add"], help="Install a plugin")
    subparsers.add_parser(
        "uninstall", aliases=["remove", "rm"], help="Uninstall a plugin")
    subparsers.add_parser(
        "update", aliases=["upgrade", "up"], help="Update a plugin")
    subparsers.add_parser(
        "list", aliases=["ls"], help="List installed plugins")
    subparsers.add_parser(
        "init", help="Initialize `rypm` to be used remotely from the bot")

    args = parser.parse_args()

    if args.command == "init":
        asyncio.run(init())
    elif args.command in ["install", "add"]:
        # Implement the logic for installing a plugin
        pass
    elif args.command in ["uninstall", "remove", "rm"]:
        # Implement the logic for uninstalling a plugin
        pass
    elif args.command in ["update", "upgrade", "up"]:
        # Implement the logic for updating a plugin
        pass
    elif args.command in ["list", "ls"]:
        # Implement the logic for listing installed plugins
        pass
    elif args.command == "help":
        parser.print_help()
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
