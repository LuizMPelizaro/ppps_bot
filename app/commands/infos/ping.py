import math

import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        @bot.tree.command(name="ping", description="Shows the bot's latency!")
        async def ping(interaction: discord.Interaction):
            # Making the latency in milliseconds and converting to int.
            bot_latency: int = math.floor((bot.latency * 1000))
            # Replying the bot's latency only to the sender user (ephemeral param)
            await interaction.response.send_message(f":ping_pong: **Bot's latency is `{bot_latency}ms`**",
                                                    ephemeral=True)


async def setup(self):
    # Adding the class as a slash command
    await self.add_cog(Ping(self))
