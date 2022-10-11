import os

import discord

from discord.ext import commands
from dotenv import load_dotenv

import conversation

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()
client = commands.Bot(command_prefix="sumire ", intents=intents)

client = discord.Client(intents=intents)

@client.event
# When a connection is established, this code will run
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channels = ["command-console"]
    if message.channel.name in channels:
        question = message.content
        answer = conversation.ask(question)
        await message.channel.send(answer)

client.run(TOKEN)
