import discord
import logging
import time

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
#intents.members(True)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_voice_state_update(self, member, before, after):
        if member == self.user:
            return

        if after.channel == None:
            targetchannel_client = await before.channel.connect()
            targetchannel_client.play(discord.FFmpegPCMAudio("kilepve.mp3", executable="C:\\ffmpeg\\bin\\ffmpeg.exe"))
            while targetchannel_client.is_playing():
                time.sleep(1)
            await targetchannel_client.disconnect()


client = MyClient(intents=intents)
client.run('BOT-TOKEN')
