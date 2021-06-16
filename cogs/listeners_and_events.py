from discord.ext import commands


class ListenersEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """Sample reaction listener. Responds with whatever emote what sent."""
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reactions = message.reactions

        emotes = []
        for reaction in reactions:
            emotes.append(f"{reaction.emoji} x {reaction.count}")

        await channel.send(
            f"{message.author.name}'s message has the following reactions!\n{', '.join(emotes)}",
            delete_after=5,
        )


def setup(bot):
    bot.add_cog(ListenersEvents(bot))
