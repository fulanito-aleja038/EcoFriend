from __future__ import annotations
import random

RECYCLE_RULES = {
    "botella plastico": "♻️ Plástico. Enjuágala y aplástala si puedes. Si tiene comida/aceite, límpiala primero.",
    "botella de agua": "♻️ Plástico. Enjuaga. La tapa depende del programa de reciclaje, pero a veces se recicla aparte.",
    "lata": "♻️ Metal/aluminio. Enjuaga y recicla.",
    "carton": "♻️ Cartón/papel. Manténlo seco. Si está grasoso (pizza), esa parte suele ir a basura/compost.",
    "papel": "♻️ Papel. Evita papel mojado o muy grasoso.",
    "vidrio": "♻️ Vidrio. Enjuaga. Ojo con vidrio roto (depende del centro).",
    "bateria": "⚠️ NO va a la basura. Llévala a un punto de recogido de baterías/e-waste.",
    "electronico": "⚠️ E-waste. Llévalo a reciclaje electrónico/punto municipal.",
    "ropa": "👕 Reusar/donar primero. Si está dañada, úsala como trapo o busca reciclaje textil.",
    "aceite": "⚠️ No lo tires por el fregadero. Guárdalo y entrégalo en recogido de aceite usado (si existe).",
    "vaso plastico": "♻️ Plástico. Enjuágalo primero y verifica si tu centro lo acepta.",
    "servilleta": "🗑️ Si está sucia, usualmente va a basura o compost si es aceptado.",
    "cartucho tinta": "⚠️ No va a la basura común. Llévalo a reciclaje de electrónicos o tienda que recoja cartuchos.",
}

DECOMPOSITION = {
    "bolsa plastico": ("Bolsa plástica", "10–20 años (o más)"),
    "botella plastico": ("Botella plástica", "~450 años"),
    "lata aluminio": ("Lata de aluminio", "80–200 años"),
    "vidrio": ("Vidrio", "miles de años (casi no se degrada)"),
    "papel": ("Papel", "semanas a meses"),
    "colilla": ("Colilla de cigarrillo", "10–12 años (y contamina mucho)"),
}

TIPS = [
    "Usa botella reusable. Una menos al zafacón hoy.",
    "Separa el reciclaje en una caja. Lo simple se mantiene.",
    "Reusar y donar casi siempre gana antes que botar.",
    "Enjuaga envases rápido. Reciclaje sucio a veces termina en basura.",
    "Evita compras con mucho empaque cuando puedas.",
]

CHALLENGES = [
    ("Sin plástico hoy", "Evita botellas/bolsas plásticas por 24h (si puedes)."),
    ("Separación express", "Separa 10 objetos reciclables y déjalos listos."),
    ("Reusar algo", "Reusa un envase en vez de botarlo (un pote, una caja)."),
    ("Compra inteligente", "Elige un producto con menos empaque."),
    ("Basura cero mini", "Haz una comida/merienda sin generar basura (o lo mínimo)."),
]

CRAFTS = [
    "Maceta con botella plástica: corta, haz drenaje y decora.",
    "Porta-lápices con lata: lava, seca y cúbrela con papel/cordel.",
    "Organizador con cajas de cartón: perfecto para gavetas/cables.",
    "Decoración con tapas: mosaicos simples o imanes (si tienes pega).",
]

def normalize(text: str) -> str:
    return " ".join(text.lower().strip().split())

def classify_item(item: str) -> str:
    key = normalize(item)

    if key in RECYCLE_RULES:
        return RECYCLE_RULES[key]

    if "bateria" in key or "pila" in key:
        return RECYCLE_RULES["bateria"]
    if "electron" in key or "celular" in key or "laptop" in key or "cargador" in key:
        return RECYCLE_RULES["electronico"]
    if "botella" in key and ("plast" in key or "plást" in key):
        return RECYCLE_RULES["botella plastico"]
    if "lata" in key:
        return RECYCLE_RULES["lata"]
    if "carton" in key or "cartón" in key or "caja" in key:
        return RECYCLE_RULES["carton"]
    if "papel" in key:
        return RECYCLE_RULES["papel"]
    if "vidrio" in key or "frasco" in key:
        return RECYCLE_RULES["vidrio"]
    if "ropa" in key or "camisa" in key or "pantalon" in key or "pantalón" in key:
        return RECYCLE_RULES["ropa"]

    return "🤔 No estoy 100% seguro. Dime el material (plástico/metal/vidrio/papel) y si está sucio con comida/aceite."

def decomposition_time(item: str) -> str:
    key = normalize(item)

    if key in DECOMPOSITION:
        name, time = DECOMPOSITION[key]
        return f"🕒 **{name}**: {time}"

    if "botella" in key and ("plast" in key or "plást" in key):
        name, time = DECOMPOSITION["botella plastico"]
        return f"🕒 **{name}**: {time}"
    if "bolsa" in key and ("plast" in key or "plást" in key):
        name, time = DECOMPOSITION["bolsa plastico"]
        return f"🕒 **{name}**: {time}"
    if "lata" in key:
        name, time = DECOMPOSITION["lata aluminio"]
        return f"🕒 **{name}**: {time}"
    if "vidrio" in key:
        name, time = DECOMPOSITION["vidrio"]
        return f"🕒 **{name}**: {time}"
    if "papel" in key or "carton" in key or "cartón" in key:
        name, time = DECOMPOSITION["papel"]
        return f"🕒 **{name}**: {time}"

    return "🕒 No lo tengo en mi lista. Prueba: botella plastico, bolsa plastico, lata aluminio, vidrio, papel, colilla."

def random_tip() -> str:
    return "🌿 Tip: " + random.choice(TIPS)

def random_challenge() -> tuple[str, str]:
    return random.choice(CHALLENGES)

def craft_idea() -> str:
    return "🎨 Idea: " + random.choice(CRAFTS)

def ascii_bar(value: int, max_value: int = 30, width: int = 14) -> str:
    if max_value <= 0:
        max_value = 1
    v = max(0, min(value, max_value))
    filled = int(round((v / max_value) * width))
    return "█" * filled + "░" * (width - filled)
