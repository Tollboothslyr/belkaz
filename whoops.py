# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import random
from discord.ext import commands
import discord
from pygame import mixer
import asyncio
TOKEN = 'NDc3NTA1NTM1MTE0MjE1NDM0.Dk9Hog.GWTwkF3rH_tCK-20q3u1LzLn0gc'


client = discord.Client()
def lvl(player, level, dist):
    if True == True:
        return True

voice = None
class voiceState:

@client.event
def __init__(self, bot):
    self.current = None
    self.voice = None
    self.bot = bot
    self.play_next_song = asyncio.Event()
    self.songs = asyncio.Queue()
    self.skip_votes = set()  # a set of user_ids that voted


async def on_message(message,):

    f = open("Levels.txt", "w+")
    I = 0  # for text file increments
    I = I + 1
    global voice
    # we do not want the bot to reply to itself
    msg = ""
    if message.author == client.user:
        return

    if message.content.startswith('$roll'):


        if message.content.endswith('d20'):

            msg = (message.author.mention + " rolled a " + str(random.randint(1,20)))
            mixer.init()
            mixer.music.load('diceroll.mp3')
            mixer.music.play()

        if message.content.endswith('d4'):

            msg = (message.author.mention + " rolled a " + str(random.randint(1, 4)))
            mixer.init()
            mixer.music.load('diceroll.mp3')
            mixer.music.play()
        if message.content.endswith('d6'):

            msg = (message.author.mention + " rolled a " + str(random.randint(1,6)))
            mixer.init()
            mixer.music.load('diceroll.mp3')
            mixer.music.play()

        if message.content.endswith('d8'):

            msg = (message.author.mention + " rolled a " + str(random.randint(1,8)))
            mixer.init()
            mixer.music.load('diceroll.mp3')
            mixer.music.play()

        if message.content.endswith('d10'):

            msg = (message.author.mention + " rolled a " + str(random.randint(1, 10)))
            mixer.init()
            mixer.music.load('diceroll.mp3')
            mixer.music.play()

        if message.content.endswith('d12'):

            msg = (message.author.mention + " rolled a " + str(random.randint(1, 12)))
            mixer.init()
            mixer.music.load('diceroll.mp3')
            mixer.music.play()
    else:
        print("AHHH")
    await client.send_message(message.channel, msg)
    voice = await bot.join_voice_channel(channel)
    player = voice.create_ffmpeg_player('fart.mp3')
    player.start()

    channel = message.author.voice.voice_channel

    await client.join_voice_channel(channel)






@client.event
async def on_ready():
    print('Rolling in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
