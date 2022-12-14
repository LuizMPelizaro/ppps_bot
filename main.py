import asyncio
import os
from app.utils.condition_utils import ConditionUtils
from app.utils.date_time_utils import get_current_time

import discord
from discord.ext import commands

from dotenv import dotenv_values

config = dotenv_values(".env")

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)
client = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"{get_current_time()} :: Logged in as {bot.user}!")


async def load():
    # Listing all files inside `app/commands/infos`
    for file_name in os.listdir("./app/commands/infos"):
        # Checking if it is a python file
        if file_name.endswith(".py"):
            # Registering the class as a slash command
            await bot.load_extension(f'app.commands.infos.{file_name[:-3]}')


@bot.command(name="sync")
async def sync(ctx):
    # Check if the author is mine (zvinniie#0484)
    if ctx.author.id == 240216596075773952:

        # Check if it's not syncing
        if not ConditionUtils.is_syncing:
            ConditionUtils.is_syncing = True

            synced = await bot.tree.sync()

            print(f"{get_current_time()} :: Synced {len(synced)} slash commands!")
            await ctx.send(f"👍 **`{len(synced)}` slash commands synced!**")

            ConditionUtils.is_syncing = False


async def main():
    await load()

    # Starts the bot using the TOKEN inside .env file
    await bot.start(config.get("TOKEN"))


asyncio.run(main())
