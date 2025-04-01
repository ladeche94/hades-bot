import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import yt_dlp as youtube_dl
import random

# Charger le token depuis les variables d'environnement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Permissions
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ========== PHRASES DE BEAUF ==========
punchlines = [
    "Si t'as pas de pastis, t'as raté ta vie.",
    "J’roule en Clio, j’fais danser les mégots.",
    "Apéro sans cacahuètes ? Crime de guerre.",
    "On respecte les gens... sauf ceux qui mettent du jus d’orange dans leur bière.",
    "T'as le flow d'une 206 tunée, c’est du bon."
]

# ========== BOT READY ==========
@bot.event
async def on_ready():
    print(f"✅ Hadès le Beauf connecté en tant que {bot.user}")

# ========== COMMANDES DE BASE ==========
@bot.command()
async def ping(ctx):
    await ctx.send("T’as pingé ? J’suis là cousin 🧢")

@bot.command()
async def tic(ctx):
    await ctx.send("Tac tac dans les oreilles, ça réveille !")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def parler(ctx, channel: discord.TextChannel, *, message: str):
    try:
        await channel.send(message)
        await ctx.send(f"🗣️ J’ai causé pour toi, champion.")
    except Exception as e:
        await ctx.send(f"❌ Y a eu un souci mon reuf : {e}")

@bot.command()
async def apero(ctx):
    await ctx.send("🍻 Apéééééroooo mon reuf ! Qui ramène les chips ?")

@bot.command()
async def pastis(ctx):
    await ctx.send("🥃 Pastis 51, température ambiante, c’est comme ça qu’on aime.")

@bot.command()
async def filsdelapub(ctx):
    phrases_pub = [
        "Y'a ceux qui roulent... et ceux qui brillent ✨",
        "C’est pas une voiture, c’est une légende.",
        "Fraîcheur intense, comme ton ex en terrasse.",
        "Une bière. Un ami. Le silence. Le respect. 🍺"
    ]
    await ctx.send(random.choice(phrases_pub))

@bot.command()
async def beauf(ctx):
    await ctx.send("🧀 " + random.choice(punchlines))

# ========== MUSIQUE ==========
ytdl_format_options = {
    'format': 'bestaudio/best',
    'noplaylist': True,
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

@bot.command()
async def play(ctx, url: str):
    if ctx.author.voice is None:
        return await ctx.send("❌ Monte dans le vocal d'abord frérot 😤")

    channel = ctx.author.voice.channel
    voice_client = ctx.voice_client

    if voice_client is None:
        try:
            voice_client = await channel.connect()
            await ctx.send("🎤 J’fais mon entrée dans le vocal, comme une légende.")
        except Exception as e:
            await ctx.send(f"❌ J’ai pas réussi à rentrer : {e}")
            return

    try:
        data = await bot.loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=True))
        if 'entries' in data:
            data = data['entries'][0]

        filename = ytdl.prepare_filename(data)
        title = data.get('title', 'Musique inconnue')

        if filename:
            source = discord.FFmpegPCMAudio(filename)
            voice_client.play(source)
            await ctx.send(f"🎶 ENVOYÉÉÉÉ : **{title}** 🔊🔥")
        else:
            await ctx.send("❌ Fichier audio perdu dans les méandres du web.")

    except Exception as e:
        await ctx.send(f"❌ J’ai pété un câble en lançant la musique : {e}")

@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send("🛑 Stop ! L’ambiance est morte. Qui a fait ça ? 😩")

# ========== GESTION DES RÔLES PAR RÉACTIONS ==========
roles_rencontre = {
    "❤️": 1356355517080928498,
    "🏴‍☠️": 1356355590955204772,
    "🔥": 1356355662057177250,
    "🧭": 1356355758073053184,
    "🌌": 1356356003591098378
}

roles_orientation = {
    "🍏": 1356356288824475779,
    "🍓": 1356356107915759616,
    "🍇": 1356356165021470860,
    "🥝": 1356356241932292106,
    "🍍": 1356361566198567013
}

roles_astrologie = {
    "♈️": 1356354469113364510,
    "♐️": 1356354566370623648,
    "♎️": 1356354767462596658,
    "♍️": 1356354812995834188,
    "♒️": 1356354921523445934,
    "♌️": 1356355047935447261,
    "♑️": 1356355094513188924,
    "♋️": 1356355158144974898,
    "♏️": 1356355212943556689,
    "♓️": 1356355270501994799,
    "♊️": 1356355325552234599,
    "♉️": 1356355392371818718
}

message_rencontre = 1356365273082499363
message_orientation = 1356365386353999952
message_astrologie = 1356365453001232515

@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return

    guild = bot.get_guild(payload.guild_id)
    emoji = str(payload.emoji)
    role_id = None

    if payload.message_id == message_rencontre:
        role_id = roles_rencontre.get(emoji)
    elif payload.message_id == message_orientation:
        role_id = roles_orientation.get(emoji)
    elif payload.message_id == message_astrologie:
        role_id = roles_astrologie.get(emoji)

    if role_id:
        role = guild.get_role(role_id)
        if role:
            await payload.member.add_roles(role)
            print(f"✅ Rôle {role.name} donné à {payload.member.display_name}")

@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)
    emoji = str(payload.emoji)
    role_id = None

    if payload.message_id == message_rencontre:
        role_id = roles_rencontre.get(emoji)
    elif payload.message_id == message_orientation:
        role_id = roles_orientation.get(emoji)
    elif payload.message_id == message_astrologie:
        role_id = roles_astrologie.get(emoji)

    if role_id:
        role = guild.get_role(role_id)
        if role:
            await member.remove_roles(role)
            print(f"❌ Rôle {role.name} retiré de {member.display_name}")

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_roles(ctx):
    try:
        channel = ctx.channel

        message = await channel.fetch_message(message_rencontre)
        for emoji in roles_rencontre:
            await message.add_reaction(emoji)

        message = await channel.fetch_message(message_orientation)
        for emoji in roles_orientation:
            await message.add_reaction(emoji)

        message = await channel.fetch_message(message_astrologie)
        for emoji in roles_astrologie:
            await message.add_reaction(emoji)

        await ctx.send("✅ Réactions ajoutées sur les 3 messages, chef !")
    except Exception as e:
        await ctx.send(f"❌ Oups, j'ai raté un truc : {e}")

# ========== LANCEMENT ==========
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Token manquant.")
