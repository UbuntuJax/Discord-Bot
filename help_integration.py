#Robot Password: OTI3MDk4NzgwNTIyNzkwOTc0.YdFSBQ.Hjft2JU_pFhyDmXKYGHaz9Ek8wk
#I want a bot which pulls random quotes from the quotes chat and sends them to whichever channel the user is in when someone types '!IShitPant'
import discord
from discord.ext import commands
import os

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Cock and Balls')
help_message = "Doxx dylan by typing one of the doxx dylan keywords. These are: \"dylan\", \"flyingluigis\", \"lewongles\", and \"cunt\". \
This function will execute itself if a week passes without anyone doxxing dylan."
general_id = 927098515782504471


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    global t0
    channel = bot.get_channel(general_id)
    msg = message.content
    if message.author == bot.user:
        return
    
    if message.content.startswith('$doxxandballs'):
        await message.channel.send(help_message)

        """if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)"""
        
    
    

bot.run(os.getenv('TOKEN'))