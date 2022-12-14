import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        @bot.tree.command(name="help", description="Show all of the Commands")
        async def help_command(interaction: discord.Interaction):
            # Creating the message embed
            embed = discord.Embed(title="👍 **Here is a list of all of my Commands**", color=discord.Color.dark_purple())

            # Making a loop in the bot commands
            for command in bot.tree.get_commands():

                # Formatting and adding the command into field's list
                embed.add_field(name=f"`/{command.name}`", value=f"> *{command.description}*", inline=True)

            # Replying the list of commands to the sender user
            await interaction.response.send_message(embed=embed)


async def setup(self):
    # Adding the class as a slash command
    await self.add_cog(Help(self))
