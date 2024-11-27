from discord.ext import commands
from discord import app_commands
import discord

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Prefix command
    @commands.command()
    async def help(self, ctx):
        await ctx.send("Available commands: `/serverinfo`, `/help`, `!serverinfo`, `!help`.")

    # Slash command
    @app_commands.command(name="help", description="Get a list of commands")
    async def slash_help(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Available commands: `/serverinfo`, `/help`, `!serverinfo`, `!help`."
        )

    async def setup(bot):
        bot.tree.add_command(self.slash_help)

def setup(bot):
    bot.add_cog(HelpCommand(bot))

