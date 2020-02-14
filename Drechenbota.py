import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import ffmpeg
from discord import FFmpegPCMAudio
from discord.utils import get
import asyncio
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="#")
path = "/home/pi/PythonScripts/Drechenbot/sources/"
Zitate_Liste = [line.rstrip('\n') for line in open(path +"Zitate.txt", encoding="utf8")]
Luegen_Liste = [line.rstrip('\n') for line in open(path +"Luegen.txt", encoding="utf8")]
Soundliste = [line.rstrip('\n') for line in open(path +"sounds.txt", encoding="utf8")]


    
@bot.event #Ausgabe um zu testen ob der Bot connected hat
async def on_ready():
    for guild in bot.guilds:
        print("Bot ist online und läuft auf " + guild.name)

#############################ZITATE#############################
@bot.command()
async def zitat(ctx):
    response = random.choice(Zitate_Liste)
    await ctx.send(response)
#############################LÜGEN#############################
@bot.command()
async def lülü(ctx):
    response = random.choice(Luegen_Liste)
    await ctx.send(response)
#############################SOUNDS#############################
@bot.command()
async def sound(ctx):
    channel = ctx.message.author.voice.channel
    vc = get(bot.voice_clients, guild=ctx.guild)
    if vc and vc.is_connected():
        await vc.move_to(channel)
    else:
        vc = await channel.connect()
        sound = random.choice(Soundliste)
        vc.play(discord.FFmpegPCMAudio(sound), after=lambda e: print('done', e))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 150
        while vc.is_playing():
                await asyncio.sleep(1)
        else:
                vc.stop()
                await ctx.send("MEDDL OFF", delete_after=5)
                
###################################
@bot.command()
async def sound_u(ctx):
    channel = ctx.message.author.voice.channel
    vc = get(bot.voice_clients, guild=ctx.guild)
    if vc and vc.is_connected():
        await vc.move_to(channel)
    else:
        vc = await channel.connect()
    for x in range(728):
        sound = random.choice(Soundliste)
        vc.play(discord.FFmpegPCMAudio(sound), after=lambda e: print('done', e))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 150
        while vc.is_playing():
                await asyncio.sleep(1)
        else:
                vc.stop()
##############################
@bot.command()
async def rnd(ctx):
    nachricht = ctx.message.content.split(" ")
    await ctx.send("Etzadla wird "+random.choice(nachricht[1:])+" gezockt")

@bot.command()
async def jein(ctx):
    x = ["Ja", "Nein"]
    await ctx.send("Der Bot sagt " + random.choice(x))
    channel = ctx.message.author.voice.channel
    vc = get(bot.voice_clients, guild=ctx.guild)
    if vc and vc.is_connected():
        await vc.move_to(channel)
    else:
        vc = await channel.connect()
        sound = "/home/pi/PythonScripts/Drechenbot/sources/jein.mp3"
        vc.play(discord.FFmpegPCMAudio(sound), after=lambda e: print('done', e))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 150
        while vc.is_playing():
                await asyncio.sleep(1)
        else:
                vc.stop()

bot.run(token)
