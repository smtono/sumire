"""
A class file used to store utility functions for the Discord API
This will mainly be used for message sending and reading, but may be expanded to include other functions

Current functionality includes:
    - Sending messages
    - Reading messages
"""

import discord
import discord.ext

def send_message(message: str, channel: discord.TextChannel):
    """
    Sends a message to a channel

    Args:
        message: str
            Message to send
        channel: discord.TextChannel
            Channel to send message to
    """
    channel.send(message)

def send_embed(embed: discord.Embed, channel: discord.TextChannel):
    """
    Sends an embed to a channel

    Args:
        embed: discord.Embed
            Embed to send
        channel: discord.TextChannel
            Channel to send embed to
    """
    channel.send(embed=embed)

def read_message(message: discord.Message, channel: discord.TextChannel):
    """
    Reads a message and stores it in the chat log

    Args:
        message: discord.Message
            Message to read
    """
    # TODO: Store message in database
