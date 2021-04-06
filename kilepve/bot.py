import discord
from discord.ext import commands
import logging
from json import load
from pathlib import Path


logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
#intents.voice_states = True

bot = commands.Bot(command_prefix='$', intents=intents)

bot.load_extension("kilepvecog")

with Path("token.json").open() as f:
    config = load(f)

token = config["token"]
bot.run(token)
