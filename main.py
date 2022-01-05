#Robot Password: OTI3MDk4NzgwNTIyNzkwOTc0.YdFSBQ.Hjft2JU_pFhyDmXKYGHaz9Ek8wk
#I want a bot which pulls random quotes from the quotes chat and sends them to whichever channel the user is in when someone types '!IShitPant'
import discord
from discord.ext import commands
import os
import random

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Cock and Balls')

doxx_word_blacklist = []

@bot.event
async def on_ready():
    bot_name_list = ["Shitting Brock's Pants", "Googling Funny Monkee", "Cock and Balls", "Doxxing Dylan", "https://www.youtube.com/user/JordanPetersonVideos", \
        "https://www.youtube.com/watch?v=1XNoiP_nZgs"]
    #bot_name = 
    bot_name = random.choice(bot_name_list)
    activity = discord.Game(name=bot_name, type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    msg = message.content
    if message.author == bot.user:
        return
    
    doxx_activation = ["dylan", "flyingluigis", "lewongles", "cunt"]
    doxx_messages = ["24 Horder", "Horder Avenue", "Dylan used to be one of the best OCE D.Vas. Point and laugh.", "https://www.google.com/maps/place/24+Horder+Ave,+Labrador+QLD+4215/@-27.9503754,153.3973667,3a,75y,174.26h,90t/data=!3m7!1e1!3m5!1sMHatMFIqA2iLPL2hsZnadg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DMHatMFIqA2iLPL2hsZnadg%26cb_client%3Dsearch.gws-prod.gps%26w%3D86%26h%3D86%26yaw%3D174.25719%26pitch%3D0%26thumbfov%3D100!7i13312!8i6656!4m5!3m4!1s0x6b910fde80b478f3:0x5d728e1be878fe4b!8m2!3d-27.9505861!4d153.3973861", \
        "GET ON POINT!!!", "FUCKING SHOOT HIM!!!"]
    if any(word in msg for word in doxx_activation):
        dylan_doxx = random.choice(doxx_messages)
        while dylan_doxx in doxx_word_blacklist:
            dylan_doxx = random.choice(doxx_messages)
        doxx_word_blacklist.append(dylan_doxx)
        if len(doxx_word_blacklist) == 3:
            doxx_word_blacklist.pop(0)
        await message.channel.send(dylan_doxx)
        print(doxx_word_blacklist)
    

bot.run(os.getenv('TOKEN'))