from modules.fetcher import get_deals
from modules.formatter import format_deal

def build_post():
    deals = get_deals()

    if not deals:
        return "Hoy no hay deals disponibles."

    best = deals[0]
    return format_deal(best)
