import dotenv
import os
import discord 
from discord.ext import commands
from discord import app_commands
import string

dotenv.load_dotenv('../.env')

intent = discord.Intents.all()
command_prefixes=['/']
bot = discord.Client(intents=intent, command_prefixes=command_prefixes)
tree = app_commands.CommandTree(bot)

#EVENTS
#initializing bot
@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=868279391074021377))
    print("Bot is connected and ready to go.")
    print("Tree has been sync'd")

#dont keep this, at least, don't keep this on an event
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "@Equinox":
         await message.channel.send("Equinox is a bot developed by Synthix Labs")

#COMMANDS
#help command
@tree.command(name="help", description="Help for commands", guild=discord.Object(id=868279391074021377))
async def help(ctx):
    ctx.send("Welcome to TaskPlanner! There are currently 3 commands available. 'Run' To set a task to become active. 'List' To see your current tasks running. and 'Help' For more information. ")

#task command
@tree.command(name="task", description="Create, Manage, View tasks", guild=discord.Object(id=868279391074021377))
async def task(ctx, arg:str, arg2:str):
    if arg == "list":
        await ctx.send("List coming soon")
    elif arg == "add":
        lists = []
        tasks = lists.append(arg)
        await ctx.send("You have successfully added" + tasks)

"""
#calendar command
@tree.command(name="calender", description="graphical calender view ", guild=discord.Object(id=868279391074021377))
async def Calender(interaction: discord.Interaction):
    for i in range(0,6):
        i + 1
        print(i)
        for i in range(0,6):
            print(i + 1)
"""

#name command
@tree.command(name="name", description="description", guild=discord.Object(id=868279391074021377))
async def slash_command(interaction: discord.Interaction):    
    await interaction.response.send_message("command")

#test command
@tree.command(name="test", description="descrip")
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

#run
bot.run(os.getenv('DISCORD_TOKEN'))
