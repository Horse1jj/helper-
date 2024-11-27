from discord.ext import commands

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has joined the server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left the server.")

def setup(bot):
    bot.add_cog(Logging(bot))

