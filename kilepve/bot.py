import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
#intents.voice_states = True

bot = commands.Bot(command_prefix='$', intents=intents)

bot.load_extension("kilepvecog")

bot.run('ODI0MzQwMzc3NTI3NjQ4MzA4.YFt8zQ._glK381Zn-sUom6MKYLO9D5mvkw')
