from discord.ext import commands

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if "badword" in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention}, watch your language!")

def setup(bot):
    bot.add_cog(AutoMod(bot))

