import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

bot.run("OTk2NzgyNjkxMjE3MzA5NzI2.GkVLih.8Noq9FH7Iq-g90oEoIDjJ3Ps8b8oJ7Ijd_tPxs")


