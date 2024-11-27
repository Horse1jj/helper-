from discord.ext import commands
from discord import app_commands
import discord

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 1. Edit Role
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def editrole(self, ctx, role: discord.Role, *, new_name):
        await role.edit(name=new_name)
        await ctx.send(f"Role `{role.name}` has been renamed to `{new_name}`.")

    # 2. Tag Edit
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def tagedit(self, ctx, old_tag: str, new_tag: str):
        # Custom implementation for tag editing (e.g., stored in DB)
        await ctx.send(f"Tag `{old_tag}` updated to `{new_tag}`.")

    # 3. Custom Embed
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def customembed(self, ctx, color: str, title: str, description: str):
        embed = discord.Embed(
            title=title,
            description=description,
            color=int(color.strip('#'), 16)
        )
        await ctx.send(embed=embed)

    # 4. Timed Announcement
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def timeannouncement(self, ctx, delay: int, *, message: str):
        await ctx.send(f"Announcement scheduled in {delay} seconds.")
        await discord.utils.sleep_until(delay)
        await ctx.send(message)

def setup(bot):
    bot.add_cog(AdminCommands(bot))


