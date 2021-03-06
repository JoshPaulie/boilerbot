import os

import discord
from discord.ext import commands
from dotenv import find_dotenv, load_dotenv

from bot_config import BotConfig
from modules.bot_init import collect_cogs, load_cogs, timestamp


intents = discord.Intents(messages=True, guilds=True, reactions=True)
bot = commands.Bot(
    command_prefix=BotConfig.prefix,
    case_insensitive=True,
    intents=intents,
)


@bot.event
async def on_ready():
    """Event that runs when bot has successfully connected"""
    print(f"{bot.user.name} is ready! [{timestamp}]")
    await bot.change_presence(activity=discord.Game(name=BotConfig.status))


@bot.event
async def on_message(message):
    """Event that checks every message for possible commands"""
    await bot.process_commands(message)


load_dotenv(find_dotenv())  # Check ./README.md for details
collect_cogs()
load_cogs(bot)
bot.run(os.getenv("DISCORD"))
