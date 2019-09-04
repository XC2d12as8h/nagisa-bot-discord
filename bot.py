import discord
from discord.ext import commands

import config

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('----------------------')
    print('Bot Nagisa está online')
    print('----------------------')

@client.event
async def on_member_join(member):
    print(f'{member} entrou no servidor!')

@client.event
async def on_member_remove(member):
    print(f'{member} saiu do servidor!')

client.run(config.nagisa_token())