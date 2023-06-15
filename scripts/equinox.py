import dotenv
import os
import discord 
from discord.ext import commands
from discord import app_commands
from pymongo.mongo_client import MongoClient

#load env vars
dotenv.load_dotenv('../.env')

#initiate discord instance
intent = discord.Intents.all()
command_prefixes=['/']
bot = discord.Client(intents=intent, command_prefixes=command_prefixes)
tree = app_commands.CommandTree(bot)

#EVENTS
#initializing bot
@bot.event
async def on_ready():

    #discord bot start
    await tree.sync(guild=discord.Object(id=868279391074021377))
    print("Bot is connected and ready to go.")
    print("Tree has been sync'd")

    #MongoDB start
    global db, collection

    client = MongoClient(os.getenv('ATLAS_URI'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        db = client['TaskDatabase']
        collection = db['TaskCollection']
    except Exception as e:
        print(e)

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
    ctx.response.send_message("Welcome to TaskPlanner! There are currently 3 commands available. 'Run' To set a task to become active. 'List' To see your current tasks running. and 'Help' For more information. ")

#task command
@tree.command(name="task", description="Create, Manage, View tasks", guild=discord.Object(id=868279391074021377))
async def task(ctx, arg:str, arg2:str=None, arg3:str=None):
    userTasks = collection.find_one({"userid":f'{str(ctx.user.id)}'})
    if (userTasks != None): #if user has a document in the database
        if arg == "list":
            taskList = ""
            for taskName, task in userTasks['tasks'].items():
                taskList = taskList + "Task: " + taskName + "\nDetails: " + task + "\n\n"
            #if you want to spew the messages out one by one, look at interaction.followup documentation
            #otherwise, you have to end the response at the first interaction.response.send_message
            await ctx.response.send_message(taskList)

        if arg == "add":
            if arg2 not in userTasks['tasks']:
                query = {"userid":f'{str(ctx.user.id)}'}
                update = {
                    '$set': {
                        f'tasks.{arg2}': arg3
                    }
                }
                collection.update_one(query, update)
                await ctx.response.send_message(f'Sucessfully added "{arg2}" to task list')
            else:
                await ctx.response.send_message(f'"{arg2}" task already exists')

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


#run
bot.run(os.getenv('DISCORD_TOKEN'))
