#https://realpython.com/how-to-make-a-discord-bot-python/

import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import random

#loads env variables from a .env file in current dir
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#different sponge-ify functions
def sponge(s):
    return ''.join(c.lower() if i % 2 == 0 else c for i, c in enumerate(s.upper()))
def spongerand(s):
    return ''.join(c.lower() if random.choice(range(1, 3)) == 1 else c for c in s.upper())

#print out info on guild and members
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
            f'{bot.user.name} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
            )

    for member in guild.members:
        print(f' - ', member.name, ' ', member.id)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await message.channel.send(spongerand(message.content))

bot.run(TOKEN)
