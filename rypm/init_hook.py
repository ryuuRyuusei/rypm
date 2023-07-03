"""
This file is part of `rypm`.

Initialize extension/cog/hook for `ryuuRyuusei` Discord bot.
"""

import os
from sys import exit as exit_

from aiohttp import ClientConnectionError, ClientSession

from rypm.commons import confirm

async def initialize():
    """Initialize `rypm` to be used remotely from the bot."""
    # check if current directory is the bot directory
    if not os.path.exists("ryuuRyuusei"):
        print("This command must be run from the bot directory.")
        exit_(1)
    ask = confirm("Are you sure you want to initialize `rypm`?", default=False)
    if ask:
        print("Initializing `rypm`...")
        # if hook already exists, delete it
        file_name = "ryuuRyuusei/extensions/rypm.py"
        if os.path.exists(file_name):
            os.remove(file_name)
        try:
            async with ClientSession() as session:
                async with session.get(
                    "https://raw.githubusercontent.com/ryuuRyuusei/rypm/main/hooks/rypm.py"
                ) as req:
                    if req.status != 200:
                        raise ConnectionError(await req.text(encoding="utf-8"))
                    with open(file_name, "w", encoding="utf-8") as file_:
                        file_.write(await req.text())
            print("Done.")
            print("Please restart the bot to apply changes.")
            exit_(0)
        except ClientConnectionError:
            print("Failed to connect to GitHub.")
            exit_(1)
        except ConnectionError as error:
            print(f"Failed to connect to GitHub. {error.args[0]}")
            exit_(1)
    print("Aborted.")
    exit_(1)


__all__ = ["initialize"]
