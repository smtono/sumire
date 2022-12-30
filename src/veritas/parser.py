"""
Contains commands for interacting with Sumire

Commands include:
    - help
    - ping
    - info
    - invite
    - talk
    - dalle
"""

import discord

from veritas import conversation, dalle

class Parser():
    
    def __init__(self) -> None:
        commands = {
            "help": self.help_command,
            "ping": self.ping_command,
        }

    def parse_command(self, args: list):
        """
        Parses a command and returns a response
        
        Args:
            args: list
                List of arguments passed by the user
        Returns:
            None
        """
        command = args[0]   # command to execute
        args = args[1:]     # args to pass to command
        
        # Get the command function
        command_function = self.commands.get(command)
        
        # If the command is not found, print an error message
        if command_function is None:
            print(f'Command {command} not found')
            return
        else:
            getattr(self, command)(args)
        

    def help_command(self):
        """
        Returns a help embed
        """
        embed = discord.Embed(
            title="Help",
            description="Sumire is a bot that can talk to you and generate images. \n\n"
        )

    def ping_command(self):
        """
        Returns ping
        """
        
    def info_command(self):
        """
        Returns an info embed about a command
        """

    def invite_command(self):
        """
        Returns an invite link
        """

    def talk_command(self, user_input: str):
        """
        Begins a conversation with the user
        
        Args:
            user_input: str
                User's input
        Returns:
            None
        """
        # Grab person talking
        
        # Check for their log in db
        
        # Possibly start a new thread? With only this person interacting
        
        # While loop until person says "stop"
        answer = conversation.ask(user_input)

    def dalle_command(self, user_input: str):
        """
        Returns a generated image
        
        Args:
            user_input: str
                User's input
        Returns:
            None
        """
        answer = dalle.ask(user_input)
