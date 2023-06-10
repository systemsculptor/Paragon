import discord
from discord import commands
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('This documentation is giving me more trouble than gentoo')

client.run(25617c5cfada36a79f143222e1bbb86ef7262db83fec6eb399934421779909cc)
