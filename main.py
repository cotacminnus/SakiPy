import os
import discord
import time
import pytz
import json
import saki

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

token = None
loc_dir = "local/"
resource_dir = "resources/"
gmt = pytz.timezone("UTC")

#Saki = saki.Staff(os.getenv("LOCDIR", "local/"))   do for .env setup

#read json
with open("config/config.json", "r") as f:  #json setup
    content = f.read()
    cfg = json.loads(content)
    token = cfg["token"]
    loc_dir = cfg["locdir"]
    gmt = pytz.timezone(cfg["gmt"])

Saki = saki.Staff(loc_dir)

intents = discord.Intents.default()
intents.message_content = True

Sakiko = discord.Client(intents=intents)

#每天0点（本地时间）定时清空
def print_current_time():
    print("现在时间:", datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"))

def clear():
    dir = os.fsencode(loc_dir)
    for f in os.listdir(dir):
        fname = os.fsdecode(f)
        if(fname.endswith(".saki")):
            open(loc_dir + fname, "w").close()

schedule = BlockingScheduler()
schedule.add_job(clear, "cron", hour=0, minute=0, timezone=gmt)

@Sakiko.event
async def on_ready():
    print('小祥上班了')
    await Sakiko.change_presence(status=discord.Status.online, activity=discord.activity.CustomActivity("客服S为您服务"))
    

@Sakiko.event
async def on_message(message):
    if message.author == Sakiko.user:
        return
    
    #なんで春日影やったの
    if "春日影" in message.content:
        time.sleep(1)
        await message.reply(file=discord.File(resource_dir + "saki_naki.png"))
    
    #名 场 面
    elif "小祥，你终于来了" in message.content:
        time.sleep(2)
        await message.reply(saki.SAKI_SOYO_0)
        time.sleep(2)
        await message.channel.send(saki.SAKI_SOYO_123)
        time.sleep(2)
        await message.channel.send(saki.SAKI_SOYO_45678)
        time.sleep(2)
        await message.channel.send(saki.SAKI_SOYO_9AB)
        time.sleep(2)
        await message.channel.send(saki.SAKI_SOYO_CDEF)
        time.sleep(2)
        await message.reply(saki.SAKI_SOYO_10)
    
    elif "我什么都会做" in message.content or "我什麼都會做" in message.content or "私にできることなら何でもする" in message.content:
        time.sleep(2)
        await message.reply(saki.SAKI_SOYO_10)

    #
    elif Sakiko.user.id in message.raw_mentions:
        #投祥
        if "投祥" in message.content:
            time.sleep(1)
            await message.reply(Saki.tousaki(message.author))
        #今日运势
        elif "今日运势" in message.content or "今日運勢" in message.content:
            time.sleep(1)
            unsei = Saki.unsei(message.author)
            if unsei == saki.UNSEI_U:
                await message.reply(unsei)
            else:
                await message.reply(file=discord.File(resource_dir + unsei))

        elif "贵安" in message.content or "貴安" in message.content or "ご機嫌よう" in message.content:
            time.sleep(1)
            await message.reply("贵安。")

        elif "祝你幸福" in message.content or "祝妳幸福" in message.content:
            time.sleep(2)
            await message.reply("祝你幸福。")

        elif "お幸せに" in message.content or "おしあわせに" in message.content or "オシアワセニ" in message.content:
            time.sleep(2)
            await message.reply("お幸せに。")
        else:
            time.sleep(1)
            await message.reply("您好，客服S为您服务。")

#客服S，启动！
print_current_time()
#clear()
Sakiko.run(token)