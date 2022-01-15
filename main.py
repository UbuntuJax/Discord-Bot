#Robot Password: OTI3MDk4NzgwNTIyNzkwOTc0.YdFSBQ.Hjft2JU_pFhyDmXKYGHaz9Ek8wk
#I want a bot which pulls random quotes from the quotes chat and sends them to whichever channel the user is in when someone types '!IShitPant'
import discord
from discord.ext import commands, tasks
import os
import random
import time
import asyncio
from itertools import cycle

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Cock and Balls')

doxx_word_blacklist = []
bot_name_blacklist = []
bot_name_list = ["Shitting Brock's Pants", "Googling Funny Monkee", "Cock and Balls", "Doxxing Dylan", "https://www.youtube.com/user/JordanPetersonVideos", \
        "https://www.youtube.com/watch?v=1XNoiP_nZgs"]
doxx_activation = ["dylan", "flyingluigis", "lewongles", "cunt"]
doxx_messages = ["24 Horder", "Horder Avenue", "Dylan used to be one of the best OCE D.Vas. Point and laugh.", "https://www.google.com/maps/place/24+Horder+Ave,+Labrador+QLD+4215/@-27.9503754,153.3973667,3a,75y,174.26h,90t/data=!3m7!1e1!3m5!1sMHatMFIqA2iLPL2hsZnadg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DMHatMFIqA2iLPL2hsZnadg%26cb_client%3Dsearch.gws-prod.gps%26w%3D86%26h%3D86%26yaw%3D174.25719%26pitch%3D0%26thumbfov%3D100!7i13312!8i6656!4m5!3m4!1s0x6b910fde80b478f3:0x5d728e1be878fe4b!8m2!3d-27.9505861!4d153.3973861", \
    "GET ON POINT!!!", "FUCKING SHOOT HIM!!!"]
help_message = "Doxx dylan by typing one of the doxx dylan keywords. These are: \"dylan\", \"flyingluigis\", \"lewongles\", and \"cunt\". \
This function will execute itself if a week passes without anyone doxxing dylan."
general_id = 927098515782504471
t0 = time.time()
dylan_id = 135341650917457920

@bot.event
async def on_ready(): 
    bot_name = random.choice(bot_name_list)
    activity = discord.Game(name=bot_name, type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    doxx_auto.start()
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    global t0
    channel = bot.get_channel(general_id)
    msg = message.content
    if message.author == bot.user:
        return
    
    if any(word in msg for word in doxx_activation):
        await doxx_him(message.channel)

    if msg.startswith('$doxxandballs'):
        await message.channel.send(help_message)

    elif msg.startswith('$d'):
        min = 1
        try:
            max = int(msg[2:len(msg)])
            roll = random.randint(min, max)
            await message.channel.send(f"You have rolled a {roll}!")
            if (message.author.id == dylan_id and roll == min) or (message.author.id != dylan_id and roll == max):
                await doxx_him(message.channel)

        except ValueError:
            await message.channel.send("This command is not in the proper form. Dice roll commands must be of the form \"d100\".")



async def doxx_him(channel, message=None):
    #global so that the function can edit t0 from within
    global t0
    #global because otherwise when the function terminates it will not remember what phrases are blacklisted
    global doxx_word_blacklist
    dylan_doxx = random.choice(doxx_messages)
    while dylan_doxx in doxx_word_blacklist:
        dylan_doxx = random.choice(doxx_messages)
    doxx_word_blacklist.append(dylan_doxx)
    if len(doxx_word_blacklist) == 3:
        doxx_word_blacklist.pop(0)
    await channel.send(dylan_doxx)
    t0 = time.time()

@tasks.loop(seconds=86400)
async def doxx_auto():
    global t0
    channel = bot.get_channel(general_id)
    time_sub = time.time() - t0
    if time_sub > 604800:
        await channel.send("Dylan hasn't been doxxed in a week!!!")
        await doxx_him(channel)

        print("doxx dylan")
        t0 = time.time()

bot.run(os.getenv('TOKEN'))