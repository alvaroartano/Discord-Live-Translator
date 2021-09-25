import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from commands import get
from libretranslatepy import LibreTranslateAPI


load_dotenv()

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_guild_join(guild):
    get.addguild(guild.id, guild.name, guild.member_count)


@client.command()
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!🏓", description=f"{round(client.latency * 1000)}ms", color=0x00ff00)

    await ctx.send(embed=embed)


@client.command()
async def setup(ctx):
    ctx.send("Perfect! ")


@client.command()
async def translate(ctx, *, text):
    lt = LibreTranslateAPI("https://translate.astian.org/")
    await ctx.send(lt.translate(text, "en", "es"))

client.run(os.getenv('DISCORD_TOKEN'))
