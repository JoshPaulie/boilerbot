from discord.ext import commands
from bot_init import timestamp


class ListenersEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_command(self, ctx):
        """Prints commands console (Example event/listener)"""
        message = ctx.message
        command = message.content
        user = message.author.name
        print(" - ".join([command, user, timestamp]))


def setup(bot):
    bot.add_cog(ListenersEvents(bot))
