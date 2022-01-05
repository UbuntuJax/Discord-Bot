#Robot Password: OTI3MDk4NzgwNTIyNzkwOTc0.YdFSBQ.Hjft2JU_pFhyDmXKYGHaz9Ek8wk
#I want a bot which pulls random quotes from the quotes chat and sends them to whichever channel the user is in when someone types '!IShitPant'
import discord
from discord.ext import commands
import os
import random

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')


@bot.event
async def on_ready():
    bot_name_list = ["Shitting Brock's Pants", "Googling Funny Monkee", "Cock and Balls", "Doxxing Dylan", "https://www.youtube.com/user/JordanPetersonVideos"]
    bot_name = random.choice(bot_name_list)
    activity = discord.Game(name=bot_name, type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print('We have logged in as {0.user}'.format(bot))

bot.run(os.getenv('TOKEN'))