import discord
from CustomClient import CustomBotClient
import CommandBot as CommandBot
from ErrorCommandManager import CommandErrHandler

def main():
    token = "TOKEN"
    intents = discord.Intents.default()
    intents.members = True

    bot = CustomBotClient(command_prefix='!')
    bot.add_cog(CommandBot.Greetings(bot))
    bot.add_cog(CommandBot.CommandGen(bot))
    bot.add_cog(CommandBot.CommandMsg(bot))
    bot.add_cog(CommandBot.CommandBot(bot))
    bot.add_cog(CommandErrHandler(bot))
    bot.run(token)


if __name__ == '__main__':
    main()