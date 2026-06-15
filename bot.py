import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

from eco_logic import (
    classify_item,
    decomposition_time,
    random_tip,
    random_challenge,
    craft_idea,
    ascii_bar,
)

EcoFriend = commands.Bot(command_prefix='!', intents=intents)

USER_STATS = {}  # user_id -> {"acciones": int, "retos": int}

def get_stats(user_id: int):
    if user_id not in USER_STATS:
        USER_STATS[user_id] = {"acciones": 0, "retos": 0}
    return USER_STATS[user_id]

@EcoFriend.event
async def on_ready():
    print(f'✅ EcoFriend conectado como {EcoFriend.user}.')

@EcoFriend.command(name="saludo")
async def saludo(ctx):
    await ctx.send("👋 ¡Hola! Soy EcoFriend. Escribe `!ayuda` para ver los comandos 🌱")

@EcoFriend.command(name="ayuda")
async def ayuda(ctx):
    await ctx.send(
        "📌 **Comandos EcoFriend**\n"
        "• `!reciclar <objeto>` → te digo dónde va (reciclaje/basura/e-waste)\n"
        "• `!tiempo <objeto>` → tiempo de descomposición aproximado\n"
        "• `!tip` → tip ecológico rápido\n"
        "• `!reto` → te doy un reto ecológico del día\n"
        "• `!listo` → marcas que completaste un reto (sube tu progreso)\n"
        "• `!manualidad` → idea para reusar materiales\n"
        "• `!progreso` → mini “gráfica” de tu progreso\n\n"
        "Ej: `!reciclar bateria` | `!tiempo botella plastico`"
    )

@EcoFriend.command(name="reciclar")
async def reciclar(ctx, *, objeto: str):
    stats = get_stats(ctx.author.id)
    stats["acciones"] += 1
    await ctx.send(classify_item(objeto))

@EcoFriend.command(name="tiempo")
async def tiempo(ctx, *, objeto: str):
    stats = get_stats(ctx.author.id)
    stats["acciones"] += 1
    await ctx.send(decomposition_time(objeto))

@EcoFriend.command(name="tip")
async def tip(ctx):
    stats = get_stats(ctx.author.id)
    stats["acciones"] += 1
    await ctx.send(random_tip())

@EcoFriend.command(name="manualidad")
async def manualidad(ctx):
    stats = get_stats(ctx.author.id)
    stats["acciones"] += 1
    await ctx.send(craft_idea())

@EcoFriend.command(name="reto")
async def reto(ctx):
    titulo, detalle = random_challenge()
    await ctx.send(
        f"✅ **Reto:** {titulo}\n"
        f"📎 {detalle}\n"
        f"Cuando lo completes, escribe `!listo` para registrarlo."
    )

@EcoFriend.command(name="listo")
async def listo(ctx):
    stats = get_stats(ctx.author.id)
    stats["retos"] += 1
    await ctx.send(f"🔥 ¡Duro! Registré tu reto. Llevas **{stats['retos']}** retos completados. 🌍")

@EcoFriend.command(name="progreso")
async def progreso(ctx):
    stats = get_stats(ctx.author.id)
    acciones = stats["acciones"]
    retos = stats["retos"]

    bar_acc = ascii_bar(acciones, max_value=30)
    bar_ret = ascii_bar(retos, max_value=15, width=14)

    await ctx.send(
        "📊 **Tu progreso EcoFriend**\n"
        f"Acciones (usar comandos): **{acciones}**\n"
        f"`{bar_acc}`\n"
        f"Retos completados: **{retos}**\n"
        f"`{bar_ret}`\n"
        "Tip: mientras más lo uses, más consciente te vuelves de lo que botas y lo que puedes cambiar 😉"
    )

EcoFriend.run("TOKEN_GOES_HERE")