# "Idea Man" version 0.2
# Created by Madison Tibbett

#library imports
from discord.ext.commands import Bot
import discord
import requests
import random
from random import randint

# supplementary
import fractal_io

# general : set bot prefix and retrieve discord token
BOT_PREFIX = ("?")

with open('./token') as tf:
    TOKEN = tf.read().strip()

# client/startup
client = Bot(command_prefix=BOT_PREFIX)

# clientside stuff - tells what bot is up to behind the scenes
@client.event
async def on_ready():
    await client.wait_until_ready()
    print("Logging in...")
    print("Username: " + str(client.user.name))
    print("Client ID: " + str(client.user.id))
    print("Current Servers:")
    for server in client.guilds:
        print(server.name)
    print("Starting...")
    print("Bot online!")
    print("----------")

@client.command(aliases=["idea"])
async def fractalidea(ctx):
    # decide between 2 and 5 things
    variation_things = randint(2,5)
    # generate a list and initialize a counter
    # ?is counter necessary?
    returned_answer = []
    # pull things from ext. file and append them to list
    for _ in range(variation_things):
        do_thing = fractal_io.get_variation_style()
        returned_answer.append(do_thing)
    # prune the output for prettiness
    returned_answer = str(returned_answer)[1:-1].replace("'", "")
    await ctx.send(returned_answer)

@client.command(aliases=["type"])
async def fractaltype(ctx):
    do_thing = fractal_io.get_fractal_type()
    await ctx.send(do_thing)

# dev tool | command shutdown: shuts down the bot from server
# MUST HAVE ROLE "BOTMASTER" TO USE
@client.command(aliases=["dev_sd"])
@discord.ext.commands.has_role('Botmaster')
async def shutdown(ctx):
    await ctx.send("Shutting down. Bye!")
    await client.logout()
    await client.close()

# command info: tells you about this bot
@client.command()
async def info(ctx):
    embed = discord.Embed(title="\"Idea Man\"", description="Gives Fractal Ideas", color=0x00cc99)
    embed.add_field(name="Version", value="0.1")
    embed.add_field(name="Author", value="Esherymack | Madison Tibbett")
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")
    embed.add_field(name="Github", value="https://github.com/Esherymack/Idea-Man")
    await ctx.send(embed=embed)

    # overwrite the help command with something pretty
client.remove_command('help')
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Idea Man", description = "Gives Fractal Ideas. Accepted commands are:", color=0x00cc99)
    embed.add_field(name="fractaltype | type", value="Gives a 'style' of fractal to create. Names are based off of DeviantArt tutorial names.", inline=False)
    embed.add_field(name="fractalidea | idea", value="Generates 2-5 variations or styles to create a fractal with.", inline=False)
    embed.add_field(name="?info", value="Gives info regarding this bot's development.", inline=False)
    embed.add_field(name="?help", value="Gives this message.", inline=False)
    await ctx.send(embed=embed)

client.loop.create_task(on_ready())

client.run(TOKEN)
