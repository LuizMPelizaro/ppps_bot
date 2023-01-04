import discord
from discord.ext import commands


class Play(commands.Cog):
    def __init__(self, bot: commands.Bot):
        @bot.tree.command(name="play", description="Plays Music in your Voice Channel")
        async def help_command(interaction: discord.Interaction):

            # Replying the list of commands to the sender user
            await interaction.response.send_message("This functionality is being developed")


async def setup(self):
    # Adding the class as a slash command
    await self.add_cog(Play(self))
