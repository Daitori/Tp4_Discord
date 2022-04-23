import discord
from discord.ext import commands

class Greetings(commands.Cog, name='Greetings module'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hey")
    async def adhoc_play(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}')
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member.mention}, nous a rejoins!')

class CommandGen(commands.Cog, name='User management module'):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="RenameUser")
    @commands.has_permissions(change_nickname=True)
    async def renameuser(self,ctx,member: discord.Member, name: str):
        await member.edit(nick=name)
        await ctx.send(f'Pseudo est passé de {member} a {member.mention} ')

class CommandMsg(commands.Cog, name='Message management module'):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="delete")
    async def delete(self,ctx,number: int):
        messages = await ctx.channel.history(limit=number +1).flatten()

        for each_message in messages:
            await each_message.delete()

    @commands.command(name="delete")
    async def delete(self,ctx,number: int):
        messages = await ctx.channel.history(limit=number +1).flatten()

        for each_message in messages:
            await each_message.delete()


class CommandBot(commands.Cog, name='Bot management module'):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="RenameBot")
    async def renamebot(self,ctx,name: str):
        await ctx.guild.me.edit(nick=name)
