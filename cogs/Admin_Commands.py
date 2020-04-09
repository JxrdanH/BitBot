import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio

class Admin_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(brief = 'Clear message', description = 'Clear a certain amount of messages')
    @has_permissions(administrator = True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{ctx.author} just cleared messages')
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please specify amount of messages to delete. \nError: {error}')
    
    @commands.command(brief = 'Kick members', description = 'Kick members from the server')
    @has_permissions(administrator = True, ban_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason = reason)
    
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please fill in all arguments, for help on this command type '?help kick'. \nError: {error}")
    
    @commands.command(brief = 'Ban members', decription = 'Ban members from the server')
    @has_permissions(administrator = True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason = reason)
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please fill in all arguments, for help on this command type '?help ban'. \nError: {error}")
    
    @commands.command(brief = 'Unban a user', description = 'Unban a user who has previously been banned')
    @has_permissions(administrator = True, ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for i in banned_users:
            user = i.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await self.ctx.guild.unban(user)
                await self.ctx.send(f'Unbanned {user.name}#{user.discriminator}')
    
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please fill in all arguments, for help on this command type '?help unban'. \nError: {error}")

def setup(commands):
    commands.add_cog(Admin_Commands(commands))