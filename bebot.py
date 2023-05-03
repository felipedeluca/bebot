# BeBot Discord bot
# May 2023
#
# Bot source code: adapted from https://www.pragnakalp.com/create-discord-bot-using-python-tutorial-with-examples/

import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send("Hello! I'm BeBot!")

    if message.content.startswith('image'):
        await message.channel.send(file=discord.File('cat.jpg'))
        await message.channel.send("Super! Now I have an image... just need to find out what to do with that!")

token = ''
with open("token.txt") as f:
    token = f.readlines()

client.run(token[0])

