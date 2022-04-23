from discord.ext import commands
from discord import Client

class CustomBotClient(commands.Bot):

    async def on_ready(self):
        print(f'{self.user.name} bot est pret!')
