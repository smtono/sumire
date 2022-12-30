"""
Sumire Bot is a chat bot that can talk to you and generate images.
Sumire reads messages and stores them to better understand you when using the talk command.
The talk command will generate a response based on the message you send.

Talk uses OpenAI's GPT-3 API to generate a response.
This is a paid service, so you will need to sign up for an account and get an API key.
Data from the talk command is stored in a database, so you can use it to train your own GPT-3 model.
This is also used as chat logs for future interactions with Sumire.

The image generation command uses OpenAI's DALL-E API to generate an image.
This is a paid service, so you will need to sign up for an account and get an API key.
This command will generate an image based on the text you send.
This image is generated using a neural network trained on millions of images.
So the results may not be what you expect.

General setup:
    - Create a virtual environment
    - Install requirements.txt
    - Create a .env file with the following variables:
        - DISCORD_TOKEN: Discord bot token
        - DISCORD_GUILD: Discord server name
        - OPENAI_API_KEY: OpenAI API key
    - Run main.py

Be sure to have a Discord server set up with a bot token.
You can do this by adding your bot through the Discord Developer Portal.
This is a free service, so you can create a bot and add it to your server.

Current commands:
    - help: Returns a help embed
    - ping: Returns ping
    - info: Returns an info embed about a command
    - invite: Returns an invite link
    - talk: Returns a response to a user's input
    - dalle: Returns a generated image

Have fun!
"""

import os

import discord

from discord.ext import commands
from dotenv import load_dotenv

from commands import parser
from veritas import conversation, dalle

# Set up global variables
ctx = {
    "database": None,
    "discord": None,
    "conversation": None,
    "dalle": None,
    "parser": None
}

#####################
#       Config      
#####################
# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Database setup
# TODO: Create database

# Parser setup
parser = parser.Parser()

# Discord Setup
intents = discord.Intents().all()
client = commands.Bot(command_prefix="sumire ", intents=intents)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Begin command parsing
@client.event
async def on_message(message):
    # Ignore messages from the bot
    if message.author == client.user:
        return

    # Command parsing start here
    supported_channels = ["general", "bot-commands" "sumire-bot"]
    if message.channel.name in supported_channels:
        user_input = message.content.split()
        await message.channel.send(parser.parse_command(user_input))

client.run(TOKEN)
