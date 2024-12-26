import discord
import os
from discord.ext import commands
from discord import Status, Activity, ActivityType
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="👋🏻・𝘄𝗲𝗹𝗰𝗼𝗺𝗲")
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}! 🎉")
        await channel.send("Here is a welcome image!")
        await channel.send("welcome_image.png")

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="👋🏻・𝘄𝗲𝗹𝗰𝗼𝗺𝗲")
    if channel:
        await channel.send(f"Goodbye {member.mention}, we hope to see you again! 👋🏻")

# Run the bot
bot.run(TOKEN)
