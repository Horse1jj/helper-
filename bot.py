import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

# Load config
import json
with open('config.json') as f:
    config = json.load(f)

# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)
tree = app_commands.CommandTree(bot)

# Load extensions
for folder in ['admin', 'automod', 'logging', 'member', 'moderator']:
    for filename in os.listdir(folder):
        if filename.endswith('.py'):
            bot.load_extension(f"{folder}.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    await tree.sync()  # Sync slash commands globally
    print("Slash commands synced!")

# Run bot
bot.run(os.getenv("BOT_TOKEN"))
