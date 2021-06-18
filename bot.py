import os
from datetime import datetime

import discord
from discord.ext import commands
from dotenv import find_dotenv, load_dotenv

from bot_config import BotConfig
from bot_init_functions import collect_cogs, load_cogs

intents = discord.Intents(messages=True, guilds=True, reactions=True)
bot = commands.Bot(
    command_prefix=BotConfig.prefix,
    case_insensitive=True,
    intents=intents,
)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")  # TODO add timestamp


@bot.event
async def on_message(message):
    await bot.process_commands(message)


env = find_dotenv()
if env is None:
    print("No .env was found. Refer to ./README.md")
    exit()
else:
    load_dotenv(env)
    collect_cogs()
    load_cogs(bot)
    bot.run(os.getenv("DISCORD"))
