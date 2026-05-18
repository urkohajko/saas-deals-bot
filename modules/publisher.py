# publisher.py
#
# Generador profesional de posts para SaaS Deals
# - Limpio
# - Modular
# - Sin Selenium
# - Compatible con Bluesky API

from modules.fetcher import get_deals
from modules.formatter import format_deal


def build_post():
    """
    Construye el post final para Bluesky.
    Devuelve un string listo para publicar.
    """
    deals = get_deals()

    if not deals:
        return "No hay deals disponibles hoy."

    best = deals[0]  # Selecciona el mejor deal
    return format_deal(best)
