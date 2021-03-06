from pathlib import Path
from datetime import datetime

"""
Objects used to load cogs during initialization
"""


def collect_cogs():
    """Recursively checks all python modules in ./cogs/ directory. All files must be valid cogs.
    Because it checks recursively, cogs can be further organized into directories"""
    files = Path("cogs").rglob("*.py")
    for file in files:
        if "__init__" not in file.name:
            yield file.as_posix()[:-3].replace("/", ".")


def load_cogs(bot):
    """Takes bot instance argument, "loads" collected cogs into it."""
    for cog in collect_cogs():
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(f"Failed to load cog {cog}\n{e}")


timestamp = datetime.now().strftime("%H:%M %Y/%m/%d")
