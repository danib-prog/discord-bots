from discord.ext import commands
import discord
import time
import asyncio


class Counter:
    num = 0
    weiterbitte = True

    async def start(self):
        while self.weiterbitte:
            # print(self.num)
            self.num += 1
            await asyncio.sleep(0.0001)


class Kilepve(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member == self.bot.user:
            return

        if after.channel == None:
            try:
                targetchannel_client = await before.channel.connect()
                targetchannel_client.play(discord.FFmpegPCMAudio("kilepve.mp3", executable="ffmpeg"))
                while targetchannel_client.is_playing():
                    time.sleep(.1)
                await targetchannel_client.disconnect()

            except discord.errors.ClientException:
                time.sleep(1.5)
                #Because 'kilepve.mp3' is about 2 seconds long, and if someone
                #disconnects while playing after a previous disconnection,
                # i don't want it to disconnect
                targetchannel_client = discord.utils.get(self.bot.voice_clients, channel=before.channel)
                await targetchannel_client.disconnect()


    @commands.command(name="count")
    async def responsetime_counter(self, ctx: commands.Context):
        counter = Counter()
        asyncio.create_task(counter.start())
        await ctx.send(content="OK")
        counter.weiterbitte = False
        finalnum = counter.num
        await ctx.send(f"I counted til {finalnum} while 'OK' was sent. Pretty cool, huh?!")

    @commands.command(name="bazmaa")
    async def reopener(self, ctx: commands.Context):
        self.bot.clear()



def setup(bot: commands.Bot):
    bot.add_cog(Kilepve(bot))
