import discord 
from discord.ext import commands
from discord import app_commands
import string

intent = discord.Intents.all()
command_prefixes=['/', '@']
bot = discord.Client(intents=intent, command_prefixes=command_prefixes) #how to activate your bot.
tree = app_commands.CommandTree(bot)
#example /write  


@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=868279391074021377))
    print("Bot is connected and ready to go.")
    print("Tree has been sync'd")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "@Equinox":
         await message.channel.send("Equinox is a bot developed by Synthix Labs")

@tree.command(name="help", description="Help for commands", guild=discord.Object(id=868279391074021377))
async def help(ctx):
    ctx.send("Welcome to TaskPlanner! There are currently 3 commands available. 'Run' To set a task to become active. 'List' To see your current tasks running. and 'Help' For more information. ")
@tree.command(name="task", description="Create, Manage, View tasks", guild=discord.Object(id=868279391074021377))
async def task(ctx, arg:str, arg2:str):
    if arg == "list":
        await ctx.send("List coming soon")
    elif arg == "add":
        lists = []
        tasks = lists.append(arg)
        await ctx.send("You have successfully added" + tasks)
@tree.command(name="calender", description="graphical calender view ", guild=discord.Object(id=868279391074021377))
async def Calender(interaction: discord.Interaction):
    for i in range(0,6):
        i + 1
        print(i)
        for i in range(0,6):
            print(i + 1)
@tree.command(name="name", description="description", guild=discord.Object(id=868279391074021377))
async def slash_command(interaction: discord.Interaction):    
    await interaction.response.send_message("command")

@tree.command(name="test", description="descrip")
async def first_command(interaction):
    await interaction.response.send_message("Hello!")
bot.run("MTA2NzI5NTIwNzE0NzcyMDc0NA.G52L22.RhkeI-feEfL8-DlrMUtiOMdUm7im4bFQUtP2oM")
