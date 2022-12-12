# This example requires the 'message_content' intent.

import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('Teste'):
            await message.channel.send("Teste")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')
