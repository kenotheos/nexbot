import discord
import os
from discord.ext import commands
from discord import Status, Activity, ActivityType

# Get the Discord bot token from the environment variable
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True  # To track member join/leave

# Set up the bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    # Send a welcome message to the '👋🏻・𝘄𝗲𝗹𝗰𝗼𝗺𝗲' channel
    channel = discord.utils.get(member.guild.text_channels, name="👋🏻・𝘄𝗲𝗹𝗰𝗼𝗺𝗲")
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}! 🎉")
        # You can also add an image URL to send along with the message
        await channel.send("Here is a welcome image!")
        # Replace 'your-image-url' with an actual image URL
        await channel.send("your-image-url")

@bot.event
async def on_member_remove(member):
    # Send a goodbye message to the '👋🏻・𝘄𝗲𝗹𝗰𝗼𝗺𝗲' channel
    channel = discord.utils.get(member.guild.text_channels, name="👋🏻・𝘄𝗲𝗹𝗰𝗼𝗺𝗲")
    if channel:
        await channel.send(f"Goodbye {member.mention}, we hope to see you again! 👋🏻")

# Run the bot
bot.run(TOKEN)
