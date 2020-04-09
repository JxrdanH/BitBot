import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Main_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(brief = 'Check bot status', description = 'Check bot status and latency')
    async def ping(self, ctx):
        await ctx.send(f"I'm here! \nMy latency is {round(self.client.latency*1000)}ms")
    
    @commands.command(brief = 'Make BitBot say something!', description = 'Make BitBot say something!')
    async def send(self, ctx, *, toSend):
        await ctx.send(toSend)
    
    @commands.command(brief = "Get BitBot's invite link", description = 'Get a link to invite BitBot to another server')
    async def invite_link(self, ctx):
        await ctx.send('My invite link is: \nhttps://discordapp.com/api/oauth2/authorize?client_id=696078015288836118&permissions=8&scope=bot')

def setup(client):
    client.add_cog(Main_Commands(client))