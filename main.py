import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import os

#Dev_Commands gives an error when loading main.py; fix this

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print("BitBot is up and ready")
    await client.change_presence(activity=discord.Game(name='With Yo Girl'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, command not found \nTo view a list of commands enter: '?help'")

@client.event
async def on_guild_join(guild):
    channel = discord.utils.get(guild.text_channels, name='general')
    await channel.send("Hi, I'm BitBot.\nMy command prefix is '?', to see a list of commands type '?help'")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('Njk2MDc4MDE1Mjg4ODM2MTE4.XojfSg.dtVTb6bPq7mxiCTM_dz0rdTcCJ0')