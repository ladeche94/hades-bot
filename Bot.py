# main.py
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import yt_dlp as youtube_dl
import random

gages = [
    "Chante le refrain de ta chanson honteuse préférée 🎤",
    "Avoue un crush Discord dans le chat 👀",
    "Balance un secret que personne ne connaît 🤫",
    "Raconte la dernière fois que t’as eu honte 😳",
    "Dis à voix haute ton dernier message privé 🥵",
    "Fais une déclaration d'amour au prochain qui parle ❤️",
    "Change ton pseudo en 'Beauf suprême' pendant 24h 🧀",
    "Tu dois répondre OUI à tout pendant 10 minutes 🔥",
    "Fais un compliment cringe à quelqu’un ici 💋",
    "Tu dois mettre un emoji 🍆 dans ton pseudo pendant 30 minutes",
    "Compliment spontané : Offrez un compliment sincère à la personne désignée par la bouteille.",
    "Regard prolongé : Maintenez un contact visuel avec cette personne pendant 30 secondes.",
    "Danse improvisée : Invitez la personne à une danse rapide et légère, sans musique.",
    "Question personnelle : Posez une question simple pour mieux connaître l’autre, comme “Quel est ton film préféré ?”",
    "Surnom affectueux : Inventez un surnom amical pour la personne et utilisez-le pendant le reste du jeu.",
    "Histoire partagée : Racontez une anecdote amusante ou touchante sur une expérience passée.",
    "Dessin rapide : Dessinez un petit portrait de la personne en une minute et montrez-lui le résultat.",
    "Déclaration fictive : Faites une déclaration d’amour exagérée et humoristique à la personne.",
    "Chanson dédiée : Chantez une courte chanson ou fredonnez un air en dédiant votre performance à la personne.",
    "Souvenir partagé : Évoquez un souvenir ou une expérience que vous aimeriez partager avec la personne à l’avenir."
]

# Nouvelles disquettes (phrases de drague)
disquettes = [
    "Es-tu affectée par le réchauffement climatique ? Car, t'es trop hot.",
    "Je te trouve un peu froide, attend que j'abbate le mur entre nous.",
    "Es-tu un prêt bancaire ? Parce que tu as capté mon intérêt !",
    "Tu crois à l’amour au premier regard ou je dois repasser une seconde fois ?",
    "J’aimerais être bigleux pour pouvoir te voir en double.",
    "Tu sais que t’es physiquement intelligente toi.",
    "Tu es prise ? Ça tombe bien je travaille chez EDF et je suis multiprise !",
    "T'es comme une biscotte... T'es craquante.",
    "Tu ne dois sûrement pas embrasser des inconnus alors faisons connaissance.",
    "Si t'étais un sandwich à McDonalds, tu serais le Mc-nifique !",
    "T'as des dents tellement belles on dirait des fausses.",
    "Eh t'es charmante ! ça t'dirait une glace à la menthe?!",
    "Attends, t'as fait tomber un truc... Tiens, c'est mon numéro !",
    "Excuse-moi, tu sais que ton corps est composé à plus de 60% d'eau ? Parce qu'il se trouve que j'ai soif.",
    "Tu veux que je te fasses un tour de magie ? Viens, je vais te montrer ma baguette !",
    "Les roses sont rouges, Les violettes sont bleues, Le fleuriste est daltonien, Mais moi j'ai un bon coup de rein.",
    "Pas la peine d'essayer de te débattre, l'amour est plus fort que nous.",
    "La différence entre ma voiture et toi, c'est que toi t'as pas besoin de néons pour briller.",
    "J'ai besoin d'un bouche à bouche car je viens de me noyer dans votre regard."
]

# Charger le token depuis les variables d'environnement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Permissions
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="📜 Commandes de Hadès", color=discord.Color.gold())
    embed.add_field(name="!ping", value="T’as pingé ? J’suis là cousin 🧢", inline=False)
    embed.add_field(name="!tic", value="Tac tac dans les oreilles, ça réveille !", inline=False)
    embed.add_field(name="!apero", value="Déclenche l’apéro sur le serveur 🍻", inline=False)
    embed.add_field(name="!pastis", value="Un hommage au Pastis 51, bien beauf comme il faut 🥃", inline=False)
    embed.add_field(name="!boulette", value="Balance le gif culte de la boulette 💥", inline=False)
    embed.add_field(name="!pub", value="Petite phrase de pub vintage façon Hadès 📺", inline=False)
    embed.add_field(name="!bouteille", value="Fais tourner la bouteille et impose un gage 🍾", inline=False)
    embed.add_field(name="!beauf", value="Balance une phrase bien beauf 🧀", inline=False)
    embed.add_field(name="!disquette", value="Sort une phrase de drague accompagnée d’un gif 💿", inline=False)
    embed.add_field(name="!setup_roles (admin)", value="Ajoute les réactions pour gérer les rôles sur les bons messages ⚙️", inline=False)
    embed.add_field(name="✨ Réponses automatiques", value="\- "santé" → "Mais pas des pieds 🍻"\n\- "verre" → "Mais pas plus haut que le bord 🥂"", inline=False)
    await ctx.send(embed=embed)

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

# ========== COMMANDES ==========
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

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if "santé" in content:
        await message.channel.send("Mais pas des pieds 🍻")
    elif "verre" in content:
        await message.channel.send("Mais pas plus haut que le bord 🥂")

    await bot.process_commands(message)

@bot.command()
async def apero(ctx):
    await ctx.send("🍻 Apéééééroooo mon reuf ! Qui ramène les chips ?")

@bot.command()
async def boulette(ctx):
    await ctx.send("💥 Oh là là... LA BOULETTE !")
    await ctx.send("https://media.tenor.com/BmFLBYjXRMwAAAAC/oh-la-boulette-as-de-la-jungle.gif")

@bot.command()
async def pub(ctx):
    phrases_pub = [
        "Y'a ceux qui roulent... et ceux qui brillent ✨",
        "C’est pas une voiture, c’est une légende.",
        "Fraîcheur intense, comme ton ex en terrasse.",
        "Une bière. Un ami. Le silence. Le respect. 🍺"
    ]
    await ctx.send(random.choice(phrases_pub))

@bot.command()
async def bouteille(ctx):
    membres = [m for m in ctx.guild.members if not m.bot]
    if len(membres) < 2:
        await ctx.send("Y’a pas assez de monde pour jouer, appelle tes potes !")
        return

    cible = random.choice(membres)
    gage = random.choice(gages)
    await ctx.send(f"🍾 La bouteille tourne sur le comptoir... et PAF ! Elle pointe **{cible.mention}** !\n💥 Gage : **{gage}**")

@bot.command()
async def beauf(ctx):
    await ctx.send("🧀 " + random.choice(punchlines))

@bot.command()
async def disquette(ctx):
    phrase = random.choice(disquettes)
    await ctx.send(f"💿 {phrase}")
    await ctx.send("https://tenor.com/view/anime-diskette-floppy-computer-insert-gif-16902274")

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
    "♈": 1356354469113364510,
    "♉": 1356355392371818718,
    "♊": 1356355325552234599,
    "♋": 1356355158144974898,
    "♌": 1356355047935447261,
    "♍": 1356354812995834188,
    "♎": 1356354767462596658,
    "♏": 1356355212943556689,
    "♐": 1356354566370623648,
    "♑": 1356355094513188924,
    "♒": 1356354921523445934,
    "♓": 1356355270501994799
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

@bot.event
async def on_member_join(member):
    role_id = 1356304122118148263  # ID du rôle 'invité'
    role = member.guild.get_role(role_id)
    if role:
        await member.add_roles(role)
        print(f"✅ Rôle 'invité' donné à {member.display_name}")
    else:
        print("❌ Rôle 'invité' introuvable.")

# ========== LANCEMENT ==========
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Token manquant.")
