from discord.ext import commands
from discord import app_commands
import discord

class ModeratorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Prefix command for banning
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned. Reason: {reason}")

    # Slash command for banning
    @app_commands.command(name="ban", description="Ban a user from the server")
    @app_commands.checks.has_permissions(ban_members=True)
    async def

