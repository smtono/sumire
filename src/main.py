import os

import discord

from discord.ext import commands
from dotenv import load_dotenv

from veritas import conversation, dalle

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

    # Command parsing start here
    channels = ["general"]
    if message.channel.name in channels:
        user_input = message.content.split()
    
    # Do generic parsing based on command in commands directory?
        if user_input[0] == "dalle":
            answer = dalle.ask(user_input[1:])
            await message.channel.send(answer)
        else:
            answer = conversation.ask(user_input[0:])
            await message.channel.send(answer)

client.run(TOKEN)
