from commands.base_command  import BaseCommand
from utils                  import get_rel_path
from time                   import sleep
import discord


# Plays music in the channel the message sender is currently in
class Play(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Music for you're ears"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        # Gets voice channel of message author
        voice_channel = message.author.voice

        channel = None
        if voice_channel != None:
            channel_name = voice_channel.channel.name
            vc = await voice_channel.channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=get_rel_path("audio/notMyMovie.mp3")))
            print(f"Playing music in {channel_name}")
            # Sleep while audio is playing.
            while vc.is_playing():
                sleep(.1)
            await vc.disconnect()
            print("disconnected")
        else:
            print("not in voice")
            await message.channel.send(f"This doesn't work unless you get in a voice channel {message.author.name}")
        # Delete command after the audio is done playing.
        await message.delete()
