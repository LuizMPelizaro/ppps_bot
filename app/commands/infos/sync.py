from discord.ext import commands

from app.utils.condition_utils import ConditionUtils
from app.utils.date_time_utils import get_current_time


class Sync(commands.Cog):
    def __init__(self, bot: commands.Bot):
        @bot.command(name="sync")
        async def sync(ctx):
            # Check if the author is me (zvinniie#0484)
            if ctx.author.id == 240216596075773952:

                # Check if it's not syncing
                if not ConditionUtils.is_syncing:
                    ConditionUtils.is_syncing = True

                    message = await ctx.send(":hourglass_flowing_sand: **Syncing commands...**")  # :hourglass:

                    synced = await bot.tree.sync()

                    await message.delete()

                    print(f"{get_current_time()} :: Synced {len(synced)} slash commands!")
                    await ctx.send(f"👍 **`{len(synced)}` slash commands synced!**")

                    ConditionUtils.is_syncing = False


async def setup(self):
    # Adding the class as a slash command
    await self.add_cog(Sync(self))
