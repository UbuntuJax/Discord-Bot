#Robot Password: OTI3MDk4NzgwNTIyNzkwOTc0.YdFSBQ.Hjft2JU_pFhyDmXKYGHaz9Ek8wk
#I want a bot which pulls random quotes from the quotes chat and sends them to whichever channel the user is in when someone types '!IShitPant'
import discord
from discord.ext import commands
import os

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(os.getenv('TOKEN'))