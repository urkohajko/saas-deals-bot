from modules.fetcher import get_deals
from modules.formatter import build_thread_for_deal, build_single_post_for_deal


def build_posts():
    """
    Devuelve una lista de hilos.
    Cada hilo es una lista de dicts:
    {
        "text": str,
        "image_url": str | None,
        "alt": str | None
    }
    """
    deals = get_deals()

    if not deals:
        return [[{"text": "Hoy no hay deals disponibles.", "image_url": None, "alt": None}]]

    threads = []

    # 1) Un hilo profundo para el mejor deal
    best = deals[0]
    threads.append(build_thread_for_deal(best))

    # 2) Un multipost simple con varios deals en un solo hilo
    if len(deals) > 1:
        parts = []
        header = "🔥 Mejores SaaS Deals de hoy:\n"
        for d in deals[:5]:
            parts.append(
                {
                    "text": build_single_post_for_deal(d, short=True),
                    "image_url": d.get("image_url"),
                    "alt": d.get("name", "SaaS deal"),
                }
            )
        # Convertimos esa lista en un hilo: primer post = header, resto = cada deal
        thread = [{"text": header, "image_url": None, "alt": None}] + parts
        threads.append(thread)

    return threads
