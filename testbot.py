import json
import os
import discord

from utils import music, utility
from discord.ext import commands
from boto.s3.connection import S3Connection

token = S3Connection(os.environ['TOKEN'])

config = utility._import("test.json")
songs = utility._import("data/music.json")
bot = commands.Bot(command_prefix=config.prefix)
bot.load_extension('utils.music')

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("\nRunning...")

@bot.command()
async def test(ctx):
    await ctx.send('I heard you! {0}'.format(ctx.author.mention))

@bot.command()
async def wotd(ctx):
    await ctx.send('Your Waifu of the Day:')

bot.run(token)
