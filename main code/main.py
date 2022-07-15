import discord
from discord.ext import commands

import json  #to save token or other things

with open('setting.json', mode='r', encoding='utf8' ) as setfile:  
    #mode = r means that the mode is read
    setdata = json.load(setfile)


bot=commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event 
async def on_member_join(member):
    channel=bot.get_channel( int(setdata['WELCOME_CHANNEL']) )
    await channel.send(f'{member} join!')

@bot.event
async def on_member_leave(member):
    channel=bot.get_channel( int(setdata['LEAVE_CHANNEL']) )
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx): #ctx means context including which server、channel and so on
    await ctx.send(f'{ round(bot.latency*1000) } (ms)') #change sec into msec


bot.run( setdata['TOKEN'] )

