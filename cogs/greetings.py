import discord
from discord.ext import commands


class Greetings(commands.Cog, name="Greetings!"):
    """Example cog"""

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="hello", aliases=["hi"])
    async def hello(self, ctx):
        """Sends a warm welcome! (Example command)"""
        name = ctx.message.author.name
        await ctx.send(f"Hello there, {name}! 👋")


def setup(bot):
    bot.add_cog(Greetings(bot))
