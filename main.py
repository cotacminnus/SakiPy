import os
import discord

intents = discord.Intents.default()
intents.message_content = True

Sakiko = discord.Sakiko(intents=intents)

@Sakiko.event
async def on_ready():
    print(f'We have logged in as {Sakiko.user}')

@Sakiko.event
async def on_message(message):
    if message.author == Sakiko.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

Sakiko.run(os.getenv("TOKEN"))