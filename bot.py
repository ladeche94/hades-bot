import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Hadès est en ligne en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong !")

if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Token manquant.")
