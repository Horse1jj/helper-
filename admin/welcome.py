from discord.ext import commands
from discord import app_commands
import discord
import json

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Event: Welcomes new members
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('config.json') as f:
            config = json.load(f)
        channel_id = config.get('welcome_channel')
        if channel_id:
            channel = self.bot.get_channel(int(channel_id))
            if channel:
                await channel.send(f"Welcome to the server, {member.mention}!")

    # Prefix command: Set the welcome channel
    @commands.command(name="setwelcome", help="Set the channel for welcome messages")
    @commands.has_permissions(administrator=True)
    async def setwelcome(self, ctx, channel: discord.TextChannel):
        with open('config.json', 'r') as f:
            config = json.load(f)
        config['welcome_channel'] = channel.id
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        await ctx.send(f"Welcome channel set to: {channel.mention}")

    # Slash command: Set the welcome channel
    @app_commands.command(name="setwelcome", description="Set the channel for welcome messages")
    @app_commands.checks.has_permissions(administrator=True)
    async def slash_setwelcome(self, interaction: discord.Interaction, channel: discord.TextChannel):
        with open('config.json', 'r') as f:
            config = json.load(f)
        config['welcome_channel'] = channel.id
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        await interaction.response.send_message(f"Welcome channel set to: {channel.mention}", ephemeral=True)

def setup(bot):
    bot.add_cog(Welcome(bot))

