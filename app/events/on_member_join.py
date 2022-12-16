import discord
from discord.ext import commands
from dotenv import dotenv_values

config = dotenv_values(".env")


class OnMemberJoin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        @bot.event
        async def on_member_join(member: discord.Member):
            guild_id = int(config.get("GUILD_ID_ADD_MEMBER"))

            # Checking if the guild id is the same of the support guild's id
            if member.guild.id == guild_id:

                # Checking if member is bot
                if member.bot:
                    # Specific role for bots
                    role_id = int(config.get("BOT_ROLE_ID_ADD_MEMBER"))
                else:
                    # Specific role for non bots
                    role_id = int(config.get("ROLE_ID_ADD_MEMBER"))

                # Looping by the guild roles
                for role in member.guild.roles:
                    # if the role id is the same of the support guild's role id
                    if role.id == role_id:
                        # Setting the role to the member
                        await member.add_roles(role)
                        continue


async def setup(self):
    # Adding the class as an event
    await self.add_cog(OnMemberJoin(self))
