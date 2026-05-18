from modules.fetcher import get_deals
from modules.formatter import (
    build_thread_for_deal,
    build_single_post_for_deal
)


def build_posts():
    """
    Devuelve SIEMPRE al menos un hilo.
    Nunca devuelve [].
    """
    deals = get_deals()

    # Si no hay deals → mensaje seguro
    if not deals:
        return [[{
            "text": "Hoy no hay deals disponibles.",
            "image_url": None,
            "alt": None
        }]]

    threads = []

    # 1) Hilo profundo del mejor deal
    best = deals[0]
    threads.append(build_thread_for_deal(best))

    # 2) Multipost con varios deals
    if len(deals) > 1:
        header = {
            "text": "🔥 Mejores SaaS Deals de hoy:",
            "image_url": None,
            "alt": None
        }

        parts = []
        for d in deals[:5]:
            parts.append({
                "text": build_single_post_for_deal(d, short=True),
                "image_url": d.get("image_url"),
                "alt": d.get("name", "SaaS deal"),
            })

        threads.append([header] + parts)

    return threads
