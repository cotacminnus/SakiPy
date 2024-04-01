import os
import discord
import json
import saki

token = None
loc_dir = None
gmt = 0

#Saki = saki.Staff(os.getenv("LOCDIR", "local/"))   do for .env setup

#read json
with open("config/config.json", "r") as f:
    content = f.read()
    cfg = json.loads(content)
    token = cfg["token"]
    loc_dir = cfg["locdir"]
    #gmt = cfg["gmt"]

Saki = saki.Staff(loc_dir)    #do for json setup

intents = discord.Intents.default()
intents.message_content = True

Sakiko = discord.Client(intents=intents)


@Sakiko.event
async def on_ready():
    print(f'We have logged in as {Sakiko.user}\n')
    await Sakiko.change_presence(status=discord.Status.online, activity=discord.activity.CustomActivity("客服S为您服务"))
    

@Sakiko.event
async def on_message(message):
    if message.author == Sakiko.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


Sakiko.run(token)
