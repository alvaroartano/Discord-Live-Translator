import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from commands import get, translate


load_dotenv()

client = commands.Bot(command_prefix='!', help_command=None)


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
async def setup(ctx, *, lang):
    if get.addChannel(ctx.guild.id, ctx.channel.id, lang) == True:
        await ctx.send("Channel set up")
    else:
        await ctx.send("This Language is not supported or the channel is already set up")


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help", description="This is the help command", color=0x00ff00)
    embed.add_field(name="!ping", value="Pong!", inline=False)
    embed.add_field(name="!setup <iso code (for example: es, fr, en, it, pt...)>",
                    value="Set up the channel. **Example for setting the actual channel to english:** `!setup en`", inline=False)
    await ctx.send(embed=embed)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):
        await client.process_commands(message)
    else:
        lang = get.checkChannel(message.channel.id)
        if lang != False:
            print(message.content)
            detection = translate.detectLanguage(message.content)
            # await message.channel.send(f"I'm {detection[0]['confidence']}% sure that that language is {detection[0]['language']}")
            if detection[0]['language'] == lang or detection[0]['confidence'] < 35:
                print(f"The language is {detection[0]['language']}")
            else:
                await message.delete()
                translation = translate.translate(message.content, lang)
                embed = discord.Embed(
                    description=f"{translation}")
                embed.add_field(name="Original message",
                                value=f"*{message.content}*")
                embed.set_footer(
                    text=f"{message.author.name}#{message.author.discriminator} said this", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

        else:
            await message.channel.send("This channel is not set up")


client.run(os.getenv('DISCORD_TOKEN'))
