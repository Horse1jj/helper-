from discord.ext import commands
from discord import app_commands
import discord
from datetime import timedelta

class ModeratorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}  # Store warnings: {user_id: [reasons]}

    # 1. Set Nickname
    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def setnickname(self, ctx, member: discord.Member, *, nickname):
        await member.edit(nick=nickname)
        await ctx.send(f"Nickname for {member.mention} set to: `{nickname}`.")

    @app_commands.command(name="setnickname", description="Set a user's nickname")
    @app_commands.checks.has_permissions(manage_nicknames=True)
    async def slash_setnickname(self, interaction: discord.Interaction, member: discord.Member, nickname: str):
        await member.edit(nick=nickname)
        await interaction.response.send_message(f"Nickname for {member.mention} set to: `{nickname}`.", ephemeral=True)

    # 2. Reset Nickname
    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def resetnickname(self, ctx, member: discord.Member):
        await member.edit(nick=None)
        await ctx.send(f"Reset nickname for {member.mention}.")

    @app_commands.command(name="resetnickname", description="Reset a user's nickname")
    @app_commands.checks.has_permissions(manage_nicknames=True)
    async def slash_resetnickname(self, interaction: discord.Interaction, member: discord.Member):
        await member.edit(nick=None)
        await interaction.response.send_message(f"Reset nickname for {member.mention}.", ephemeral=True)

    # 3. Kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked. Reason: `{reason}`.")

    @app_commands.command(name="kick", description="Kick a user from the server")
    @app_commands.checks.has_permissions(kick_members=True)
    async def slash_kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member.mention} has been kicked. Reason: `{reason}`.", ephemeral=True)

    # 4. Timeout
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: discord.Member, minutes: int, *, reason=None):
        duration = timedelta(minutes=minutes)
        await member.timeout_for(duration, reason=reason)
        await ctx.send(f"{member.mention} has been timed out for {minutes} minutes. Reason: `{reason}`.")

    @app_commands.command(name="timeout", description="Timeout a user for a specific duration")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def slash_timeout(self, interaction: discord.Interaction, member: discord.Member, minutes: int, reason: str = None):
        duration = timedelta(minutes=minutes)
        await member.timeout_for(duration, reason=reason)
        await interaction.response.send_message(f"{member.mention} has been timed out for {minutes} minutes. Reason: `{reason}`.", ephemeral=True)

    # 5. Untimeout
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def untimeout(self, ctx, member: discord.Member):
        await member.timeout(None)  # Remove timeout
        await ctx.send(f"{member.mention} has been untimed.")

    @app_commands.command(name="untimeout", description="Remove timeout for a user")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def slash_untimeout(self, interaction: discord.Interaction, member: discord.Member):
        await member.timeout(None)  # Remove timeout
        await interaction.response.send_message(f"{member.mention} has been untimed.", ephemeral=True)

    # 6. Warn
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        if member.id not in self.warnings:
            self.warnings[member.id] = []
        self.warnings[member.id].append(reason)
        await ctx.send(f"{member.mention} has been warned. Reason: `{reason}`.")

    @app_commands.command(name="warn", description="Warn a user for misconduct")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def slash_warn(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        if member.id not in self.warnings:
            self.warnings[member.id] = []
        self.warnings[member.id].append(reason)
        await interaction.response.send_message(f"{member.mention} has been warned. Reason: `{reason}`.", ephemeral=True)

    # 7. Check Warnings
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def checkcase(self, ctx, member: discord.Member):
        reasons = self.warnings.get(member.id, [])
        if not reasons:
            await ctx.send(f"{member.mention} has no warnings.")
        else:
            warnings_list = "\n".join(f"{idx + 1}. {reason}" for idx, reason in enumerate(reasons))
            await ctx.send(f"{member.mention}'s warnings:\n{warnings_list}")

    @app_commands.command(name="checkcase", description="Check warnings for a user")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def slash_checkcase(self, interaction: discord.Interaction, member: discord.Member):
        reasons = self.warnings.get(member.id, [])
        if not reasons:
            await interaction.response.send_message(f"{member.mention} has no warnings.", ephemeral=True)
        else:
            warnings_list = "\n".join(f"{idx + 1}. {reason}" for idx, reason in enumerate(reasons))
            await interaction.response.send_message(f"{member.mention}'s warnings:\n{warnings_list}", ephemeral=True)

def setup(bot):
    bot.add_cog(ModeratorCommands(bot))
