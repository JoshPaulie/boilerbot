import os

import discord
from discord.ext import commands
from dotenv import find_dotenv, load_dotenv

from bot_config import BotConfig
from init_functions import collect_cogs, load_cogs, launch_time

intents = discord.Intents(messages=True, guilds=True, reactions=True)
bot = commands.Bot(
    command_prefix=BotConfig.prefix,
    case_insensitive=True,
    intents=intents,
)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready! [{launch_time}]")


@bot.event
async def on_message(message):
    await bot.process_commands(message)


load_dotenv(find_dotenv())  # Check ./README.md for details
collect_cogs()
load_cogs(bot)
bot.run(os.getenv("DISCORD"))
