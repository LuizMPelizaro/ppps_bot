import asyncio
import os
from app.utils.date_time_utils import get_current_time
import discord
from discord.ext import commands
from dotenv import dotenv_values

config = dotenv_values(".env")
token = config.get("TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="--", intents=intents)
client = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"{get_current_time()} :: Logged in as {bot.user}!")


async def load_commands():
    print(f"{get_current_time()} :: Loading commands")
    # Listing all files inside `app/commands`
    for base_dir_name in os.listdir("./app/commands"):
        # Listing all files inside the respective directory
        for file_name in os.listdir(f"./app/commands/{base_dir_name}"):
            # Checking if it is a python file
            if file_name.endswith(".py"):
                # Registering the class as a slash command
                await bot.load_extension(f'app.commands.{base_dir_name}.{file_name[:-3]}')


async def load_events():
    print(f"{get_current_time()} :: Loading events")
    # Listing all files inside the respective directory
    for file_name in os.listdir("./app/events"):
        # Checking if it is a python file
        if file_name.endswith(".py"):
            # Registering the class as an event
            await bot.load_extension(f'app.events.{file_name[:-3]}')


async def main():
    await load_commands()
    await load_events()

    # Starts the bot using the TOKEN inside .env file
    await bot.start(token)


asyncio.run(main())
