import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import yt_dlp as youtube_dl
import random
import asyncio
import random
import json
import os

utilisateurs_ajout = {}

salon_alertes_id = 1359933488324809067

if os.path.exists("livres.json"):
    with open("livres.json", "r", encoding="utf-8") as f:
        livres_a_deviner = json.load(f)
else:
    livres_a_deviner = []

def sauvegarder_livres():
    with open("livres.json", "w", encoding="utf-8") as f:
        json.dump(livres_a_deviner, f, ensure_ascii=False, indent=4)

scores = {}

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
    "T’as pas une carte ? Parce que je me perds dans tes yeux."
    "T’es comme l’électricité… Tu me fais des étincelles dès que tu m’effleures."
    "Si la beauté était un crime, tu serais déjà en prison à perpétuité."
    "Tu dois être une mise à jour, parce que depuis que je t’ai vue, tout bug autour de moi."
    "T’as une attestation ? Parce que t’as clairement dépassé les limites de la beauté autorisée."
    "T'es pas une pizza, mais j’te prendrais bien avec supplément câlins."
    "Même Google ne pourrait pas me trouver quelqu’un comme toi."
    "Si t’étais une appli, tu serais payante. Et je m’abonnerais à vie."
    "T’as un prénom, ou je peux t’appeler mienne ?"
    "Je suis pas photographe, mais je peux nous voir ensemble."
]

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

if os.path.exists("scores.json"):
    with open("scores.json", "r", encoding="utf-8") as f:
        scores = json.load(f)
else:
    scores = {}

def sauvegarder_scores():
    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=4)
        
# ========== PHRASES DE BEAUF ==========
punchlines = [
    "Tant que je tiens debout, je suis pas bourré(e)"
"Je suis comme le bon vin, plus je vieillis, plus je suis excellent(e)"
"Le seul enchaînement que je fais ici: c’est café, boulot, râler"
"Bonjour à tout le monde, sauf ceux qui disent \"pain au chocolat ou chocolatine\" (histoire de bien relancer le débat pourri hihi)"
]


# ========== BOT READY ==========
@bot.event
async def on_ready():
    print(f"✅ Hadès le Beauf connecté en tant que {bot.user}")

# ========== COMMANDES ==========
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="📜 Commandes de Hadès", color=discord.Color.gold())
    embed.add_field(name="!ping", value="T’as pingé ? J’suis là cousin 🧢", inline=False)
    embed.add_field(name="!tic", value="Tac tac dans les oreilles, ça réveille !", inline=False)
    embed.add_field(name="!apero", value="Déclenche l’apéro sur le serveur 🍻", inline=False)
    embed.add_field(name="!boulette", value="Balance le gif culte de la boulette 💥", inline=False)
    embed.add_field(name="!pub", value="Petite phrase de pub vintage façon Hadès 📺", inline=False)
    embed.add_field(name="!bouteille", value="Fais tourner la bouteille et impose un gage 🍾", inline=False)
    embed.add_field(name="!beauf", value="Balance une phrase bien beauf 🧀", inline=False)
    embed.add_field(name="!disquette", value="Sort une phrase de drague accompagnée d’un gif 💿", inline=False)
    embed.add_field(name="!pfc [pierre|feuille|ciseaux]", value="Pierre-Feuille-Ciseaux contre Hadès ✊📄✂️", inline=False)
    embed.add_field(name="!devine", value="Hadès pense à un nombre entre 1 et 100. À toi de deviner ! 🔢", inline=False)
    embed.add_field(name="!livre", value="Devine un livre à partir d’un indice 📖", inline=False)
    embed.add_field(name="!propose [réponse]", value="Fais ta proposition pour le jeu du livre 🕵️", inline=False)
    embed.add_field(name="!score", value="Affiche ton score dans le jeu 'Devine le livre' 🧠", inline=False)
    embed.add_field(name="!classement", value="Montre le classement des meilleurs joueurs 📊", inline=False)
    embed.add_field(name="!ajoute_livre (en MP)", value="Propose un nouveau livre à deviner 💌", inline=False)
    embed.add_field(name="!eightball [question]", value="Pose une question à la boule magique 🎱", inline=False)
    embed.add_field(name="!lovecalc @pseudo1 @pseudo2", value="Calcule la compatibilité amoureuse entre deux personnes 💘", inline=False)
    embed.add_field(name="!setup_roles (admin)", value="Ajoute les réactions pour gérer les rôles sur les bons messages ⚙️", inline=False)
    embed.add_field(
        name="✨ Réponses automatiques",
        value="• Tape **santé** → Hadès répond *Mais pas des pieds 🍻*\n"
              "• Tape **verre** → Hadès répond *Mais pas plus haut que le bord 🥂*",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command()
async def livre(ctx):
    livre = random.choice(livres_a_deviner)
    ctx.bot.devine_livre_en_cours = livre  # On garde l'énigme active
    await ctx.send(f"📖 **Devine le livre :**\n*{livre['indice']}*\n\nTape `!propose [ta réponse]` pour jouer !")

@bot.command()
async def propose(ctx, *, proposition):
    livre = getattr(ctx.bot, "devine_livre_en_cours", None)
    if not livre:
        await ctx.send("📚 Il n'y a pas de livre à deviner pour l'instant. Lance le jeu avec `!livre`.")
        return

    if proposition.lower().strip() == livre["reponse"].lower():
        sauvegarder_scores()
        user_id = str(ctx.author.id)
        scores[user_id] = scores.get(user_id, 0) + 1
        await ctx.send(f"🎉 Bravo {ctx.author.mention} ! C’était **{livre['reponse']}**. Tu gagnes 1 point ! 🏆\nTu as maintenant {scores[user_id]} point(s) !")
        ctx.bot.devine_livre_en_cours = None
    else:
        await ctx.send(f"❌ Mauvaise réponse, {ctx.author.mention}. Essaie encore !")

@bot.command()
async def score(ctx):
    user_id = str(ctx.author.id)
    score = scores.get(user_id, 0)
    await ctx.send(f"📊 {ctx.author.mention}, tu as **{score} point(s)**.")

@bot.command()
async def classement(ctx):
    if not scores:
        await ctx.send("🪶 Aucun score enregistré pour le moment.")
        return

    classement = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    message = "🏆 **Top 5 des détectives littéraires** 📚\n\n"

    for i, (user_id, score) in enumerate(classement[:5], start=1):
        user = await bot.fetch_user(int(user_id))
        message += f"{i}. {user.name} — {score} point(s)\n"

    await ctx.send(message)

@bot.command()
async def dernier_livre(ctx):
    if livres_a_deviner:
        dernier = livres_a_deviner[-1]
        await ctx.send(f"🕵️‍♂️ **Dernier livre ajouté :**\nIndice : *{dernier['indice']}*\nRéponse : ||{dernier['reponse']}||")
    else:
        await ctx.send("Aucun livre enregistré.")
        
@bot.command()
async def eightball(ctx, *, question: str):
    reponses = [
        "Sans aucun doute, cousin.",
        "Faut voir avec le pastis d'abord.",
        "Hmm... J’dirais que oui, mais j’suis pas devin hein.",
        "T'as p'têt plus de chances au loto.",
        "Pose ta question après l’apéro.",
        "Grave possible, comme un kebab à 4h du mat.",
        "C’est chaud mon reuf, mais qui ne tente rien...",
        "Oublie, même les astres rigolent."
    ]
    await ctx.send(f"🎱 Question : {question}\nRéponse : {random.choice(reponses)}")

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

    # ✅ ICI : gestion des DM pour ajout de livre
    if isinstance(message.channel, discord.DMChannel):
        uid = message.author.id
        if uid in utilisateurs_ajout:
            etat = utilisateurs_ajout[uid]

            if etat["step"] == 1:
                etat["indice"] = message.content
                etat["step"] = 2
                await message.channel.send("✍️ Parfait ! Maintenant, envoie-moi **le titre exact du livre**.")
            elif etat["step"] == 2:
                etat["reponse"] = message.content
                livres_a_deviner.append({
                    "indice": etat["indice"],
                    "reponse": etat["reponse"]
                })
                sauvegarder_livres()

                # Envoie une alerte dans le salon d'alertes
                for guild in bot.guilds:
                    salon = guild.get_channel(salon_alertes_id)
                    if salon:
                        await salon.send(
                            f"📚 **Nouveau livre proposé par {message.author.mention}** :\n"
                            f"🔍 Indice : *{etat['indice']}*\n"
                            f"✅ Réponse : **{etat['reponse']}**"
                        )

                del utilisateurs_ajout[uid]
                await message.channel.send("✅ Livre ajouté avec succès ! Merci pour ta contribution 💖")

    await bot.process_commands(message)

@bot.command()
async def ajoute_livre(ctx):
    if not isinstance(ctx.channel, discord.DMChannel):
        await ctx.send("📥 Envoie cette commande **en MP** à Hadès pour ajouter un livre.")
        return

    utilisateurs_ajout[ctx.author.id] = {"step": 1}
    await ctx.send("📚 Super ! Envoie-moi maintenant **l’indice** du livre (citation ou résumé).")


@bot.command()
async def apero(ctx):
    await ctx.send("🍻 Apéééééroooo mon reuf ! Qui ramène les chips ?")

@bot.command()
async def pfc(ctx, choix: str):
    options = ["pierre", "feuille", "ciseaux"]
    if choix.lower() not in options:
        return await ctx.send("❌ Choisis entre `pierre`, `feuille` ou `ciseaux`, champion !")

    bot_choix = random.choice(options)
    await ctx.send(f"🧠 Hadès a choisi : **{bot_choix}**")

    if choix == bot_choix:
        await ctx.send("🤝 Égalité ! T'es pas si nul.")
    elif (choix == "pierre" and bot_choix == "ciseaux") or \
         (choix == "feuille" and bot_choix == "pierre") or \
         (choix == "ciseaux" and bot_choix == "feuille"):
        await ctx.send("🔥 T'as gagné ! Une petite bière pour fêter ça ?")
    else:
        await ctx.send("💀 Boum ! Hadès gagne, comme d'hab.")


@bot.command(name='boulette')
async def boulette(ctx):
    await ctx.send('💥 Oh là là... LA BOULETTE !')
    await ctx.send('https://tenor.com/view/oh-la-boulette-as-de-la-jungle-roger-roger-le-jardinier-gif-11065058356198134565')

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
async def devine(ctx):
    nombre = random.randint(1, 100)
    await ctx.send("🤔 J'ai pensé à un nombre entre 1 et 100. Essaye de deviner !")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

    try:
        for _ in range(5):  # 5 tentatives max
            guess = await bot.wait_for("message", check=check, timeout=30.0)
            guess = int(guess.content)

            if guess == nombre:
                await ctx.send("🎉 Gagné ! Tu lis dans mes pensées ou quoi ?")
                return
            elif guess < nombre:
                await ctx.send("🔼 Trop petit !")
            else:
                await ctx.send("🔽 Trop grand !")

        await ctx.send(f"😏 C'était **{nombre}**. Reviens t'entraîner.")
    except asyncio.TimeoutError:
        await ctx.send(f"⏰ Trop long ! Le nombre était **{nombre}**.")

@bot.command()
async def lovecalc(ctx, user1: discord.Member, user2: discord.Member):
    pourcentage = random.randint(0, 100)

    if pourcentage >= 90:
        commentaire = "🔥 Vous êtes comme une merguez et un barbecue : inséparables et bien grillés."
    elif pourcentage >= 70:
        commentaire = "❤️ Vous êtes comme le pastis et l’eau – à consommer sans modération."
    elif pourcentage >= 50:
        commentaire = "💘 Y’a du potentiel, mais faudra bosser le romantisme mon reuf."
    elif pourcentage >= 30:
        commentaire = "😬 C’est pas fou... mais avec un apéro, tout est possible."
    else:
        commentaire = "❌ Comme deux bouteilles vides : y’a plus rien à faire..."

    await ctx.send(f"💘 Calcul en cours pour {user1.display_name} et {user2.display_name}...")
    await ctx.send(f"❤️ Résultat : **{pourcentage}%** de compatibilité !\n{commentaire}")

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
