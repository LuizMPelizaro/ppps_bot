import math
from datetime import datetime

import discord
from discord.ext import commands
from app.utils.date_time_utils import DateTimeUtils


class Uptime(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        @bot.tree.command(name="uptime", description="Show the Bot's uptime!")
        async def uptime(interaction: discord.Interaction):
            # Converting datetime to a long timestamp
            timestamp = datetime.timestamp(DateTimeUtils.get_started_at())
            # Replying the bot uptime only to the sender user (ephemeral param)
            await interaction.response.send_message(
                f"⬆️⏳ **I'm running since <t:{math.floor(timestamp)}:F> and was started "
                f"<t:{math.floor(timestamp)}:R>!**", ephemeral=False)


async def setup(self):
    # Adding the class as a slash command
    await self.add_cog(Uptime(self))
