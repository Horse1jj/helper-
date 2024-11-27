from discord.ext import commands
from discord import app_commands
import discord

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Prefix command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def serverinfo(self, ctx):
        guild = ctx.guild
        await ctx.send(f"Server Name: {guild.name}\nMember Count: {guild.member_count}")

    # Slash command
    @app_commands.command(name="serverinfo", description="Get server information")
    async def slash_serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        await interaction.response.send_message(
            f"Server Name: {guild.name}\nMember Count: {guild.member_count}"
        )

    async def setup(bot):
        bot.tree.add_command(self.slash_serverinfo)

def setup(bot):
    bot.add_cog(AdminCommands(bot))

