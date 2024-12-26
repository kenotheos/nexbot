import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='👋🏻・𝘄𝗲𝗹𝗰𝗼𝗺𝗲')
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}! 🎉")
        await channel.send(file=discord.File('welcome_image.png'))
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name='👋🏻・𝘄𝗲𝗹𝗰𝗼𝗺𝗲')
    if channel:
        await channel.send(f"Goodbye {member.mention}! We'll miss you! 😢")
        # Optionally, send an image
        await channel.send(file=discord.File('goodbye_image.png'))
bot.run(os.getenv('DISCORD_TOKEN'))