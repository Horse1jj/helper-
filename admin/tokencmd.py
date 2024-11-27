from discord.ext import commands
from discord import app_commands
import discord
import json

class PrefixCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Prefix command: Change bot prefix
    @commands.command(name="setprefix", help="Change the bot's prefix")
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, new_prefix):
        with open('config.json', 'r') as f:
            config = json.load(f)
        config['prefix'] = new_prefix
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        self.bot.command_prefix = new_prefix  # Update the bot's runtime prefix
        await ctx.send(f"Prefix successfully changed to: `{new_prefix}`")

    # Slash command: Change bot prefix
    @app_commands.command(name="setprefix", description="Change the bot's prefix")
    @app_commands.checks.has_permissions(administrator=True)
    async def slash_setprefix(self, interaction: discord.Interaction, new_prefix: str):
        with open('config.json', 'r') as f:
            config = json.load(f)
        config['prefix'] = new_prefix
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        self.bot.command_prefix = new_prefix  # Update the bot's runtime prefix
        await interaction.response.send_message(f"Prefix successfully changed to: `{new_prefix}`", ephemeral=True)

def setup(bot):
    bot.add_cog(PrefixCommands(bot))

