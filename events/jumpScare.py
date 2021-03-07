import discord

from utils                  import get_rel_path
from time                   import sleep
from random                 import random

class JumpScare:

    def __init__(self):
        pass

    async def run(self, member):
        if(random() > 0.9):
            # Gets voice channel of message author
            voice_channel = member.voice

            if voice_channel != None:
                voice_channel = voice_channel.channel
                if len(voice_channel.members) == 1:
                    vc = await voice_channel.connect()
                    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=get_rel_path("audio/death.wav")))
                    print(f"Spooking {member.name} in {voice_channel.name}")
                    # Sleep while audio is playing.
                    while vc.is_playing():
                        sleep(.1)
                    await vc.disconnect()
                    print(f"Disconnected from {voice_channel.name}")