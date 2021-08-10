# Bot launch Script
# Imports
import discord, os, datetime
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

bot.run(TOKEN)
