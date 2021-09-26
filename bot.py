import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from commands import get, translate


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
    await ctx.send("Perfect! Please let me ask you some questions.")
    questionembed = discord.Embed(
        title="Language that has to be spoken here", description="Please search your ISO 639-1 code [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) and send it as it is. For example (en, es, ru, fr, it...)", color=0x00ff00)
    await ctx.send(embed=questionembed)
    question = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    lang = question.content
    if get.addChannel(ctx.guild.id, ctx.channel.id, lang):
        await ctx.send("Perfect! This channel is set up")
    else:
        await ctx.send("This Language is not supported")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):
        await client.process_commands(message)
    else:
        lang = get.checkChannel(message.channel.id)
        if lang != False:
            await message.channel.send("Wait... Analyzing message...")
            detection = translate.detectLanguage(message.content)
            await message.channel.send(f"I'm {detection[0]['confidence']}% sure that that language is {detection[0]['language']}")
            await message.channel.send(f"{lang} can only be talked here")
        else:
            await message.channel.send("This channel is not set up")


client.run(os.getenv('DISCORD_TOKEN'))
