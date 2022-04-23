import asyncio
from dis import disco
from io import BytesIO
import discord
import logger
from discord.ext import commands
##Les variables quon rajoute sont oublier quand on redemarre, on pourrait utiliser un fichier ou json
L=[]
infractions = {}
limit = 5

class Greetings(commands.Cog, name='Greetings module'):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="hey") ##Pour tester si il est active
    async def adhoc_play(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}')
        
    @commands.Cog.listener() ##Marche pas
    async def on_member_join(self,ctx, member): 
        await ctx.send(f'{member.mention}, nous a rejoins!')

class CommandUser(commands.Cog, name='User management module'):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="RenameUser")
    @commands.has_permissions(change_nickname=True)
    async def renameuser(self,ctx,member: discord.Member, Newname: str):
        await member.edit(nick=Newname)
        await ctx.send(f'Pseudo est passé de {member} a {member.mention} ')
    
    @commands.command(name="Kick")
    async def KickUser(self,ctx,member: discord.Member):
        await member.kick()
        await ctx.send(f'{member.mention} a été kick')
    
    @commands.command(name="Ban")
    async def BanUser(self,ctx,member: discord.Member):
        await member.ban()
        await ctx.send(f'{member.mention} a été banni')

class CommandMsg(commands.Cog, name='Message management module'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="delete")
    async def delete(self,ctx,number: int):
        messages = await ctx.channel.history(limit=number +1).flatten()
        for each_message in messages:
            await each_message.delete()

    @commands.command(name="AddBadWord")  ##Les mots dans la liste sont oublier quand on redemarre, on pourrait utiliser un fichier ou json
    async def AddWord(self,ctx,Word: str):
        L.append(Word)
        await ctx.send(f'{Word} a été rajouté dans la liste')
    
    @commands.command(name="RemoveBadWord")
    async def RemoveWord(self,ctx,Word: str):
        L.remove(Word)
        await ctx.send(f'{Word} a été enlevé de la liste')
    
    @commands.command(name="ShowBadWord")
    async def ShowList(self,ctx):
        list=" ".join(str(x) for x in L)            
        await ctx.send(f'Les mots suivant sont interdits: {list} ')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.guild_permissions.administrator==False: ##Pour eviter davoir des infractions pour les admins
            msg = message.content
            for word in L:
                if word in msg: 
                    id = message.author.id
                    infractions[id] = infractions.get(id, 0) + 1
                    await message.delete()
                    warning = f"Attention {message.author.mention}, vous avez {infractions[id]} sur 5 infractions"
                    await message.channel.send(warning)                        
                    if infractions[id] >= limit:
                        await message.author.kick()

class CommandBot(commands.Cog, name='Bot management module'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="RenameBot")
    async def renamebot(self,ctx,name: str):
        await ctx.guild.me.edit(nick=name)

class CommandLogger(commands.Cog, name='Log management module'):
    @commands.command(name="Log")
    async def log(self,ctx,c: str):
        channel = discord.utils.get(ctx.guild.channels, name=c)
        channel_id = channel.id
        await ctx.channel.send(channel_id)