# Bot launch Script
# Imports
import discord, os, datetime
import databaseservice as ds
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands


print("Launching Server...")

# Load the Enviroment
load_dotenv()

# Grabbing discord token from the enviroment
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!', description="Discord Dungeons")
print("Launch Success")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def createAct(ctx):
  await ds.newuser(ctx.author.id)
    
@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
    
bot.run(TOKEN)
