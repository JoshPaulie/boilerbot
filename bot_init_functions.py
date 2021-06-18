from pathlib import Path
from datetime import datetime

"""
Objects used to load cogs during initialization
"""


def collect_cogs():
    files = Path("cogs").rglob("*.py")
    for file in files:
        if "__init__" not in file.name:
            yield file.as_posix()[:-3].replace("/", ".")


def load_cogs(bot):
    for cog in collect_cogs():
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(f"Failed to load cog {cog}\n{e}")


launch_time = datetime.now().strftime("%H:%M %Y/%m/%d")
