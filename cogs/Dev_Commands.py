import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

s = [
    'Thank you.',
    'Have a nice day.',
    'I was up late last night too. The semester is almost over. Ive had exams all week.',	
    'Yes, hes married.',
    'Do you often listen to audiobooks?',
    'I think Im losing my mind.	',
    'Id like to go to London someday.'	,
    'Ill be absent tomorrow.'	,
    'Wait until tomorrow morning.'	,
    'He hurt his knee when he fell.'	,
    'I am afraid to go.	',
    'I often refer to the dictionary.'	,
    'We couldnt go out because of the snowstorm.'	,
    'Show me another watch.	',
    'Nothing special, just working. Why do you ask?'	,
    'He can run faster than me.	',
    'I took the children to school.'	,
    'They are both good.',
    'What he said turned out to be true.'	,
    'She has never gone on a date with him.'	,
    'Could we have a table by the window?'	,
    'The Boston Celtics.']

class Dev_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief = 'Add Text for testing', description = 'Adds a series of lines for testign commands like clear.')
    @has_permissions(administrator = True)
    async def add_text(self, ctx, alias = "add text"):
        for i in s:
            await ctx.send(i)
    
    @commands.command(brief = 'Reload a cog', description = 'Reload a cog to enable changes')
    @has_permissions(administrator = True)
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f'"{extension}" reloaded')
    
def setup(client):
    client.add_cog(Dev_Commands(client))