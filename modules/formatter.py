def format_deal_long(deal):
    name = deal["name"]
    price = deal["price"]
    old = deal.get("old_price") or ""
    link = deal["link"]

    line_old = f"💸 Antes: {old}\n" if old else ""
    return (
        f"🔥 {name}\n"
        f"{line_old}"
        f"✅ Ahora: {price}\n\n"
        f"🔗 {link}\n"
        f"#SaaS #Deals #Ofertas"
    )


def format_deal_short(deal):
    name = deal["name"]
    price = deal["price"]
    link = deal["link"]

    return f"• {name} → {price}  {link}"


def build_thread_for_deal(deal):
    """
    Devuelve un hilo (lista de partes) para un solo deal.
    Cada parte: {"text", "image_url", "alt"}
    """
    parts = []

    # Intro
    intro = (
        f"🚀 SaaS destacado de hoy:\n\n"
        f"{deal['name']}\n"
        f"Precio actual: {deal['price']}\n"
    )
    parts.append(
        {
            "text": intro,
            "image_url": deal.get("image_url"),
            "alt": deal.get("name", "SaaS deal"),
        }
    )

    # Detalle largo
    parts.append(
        {
            "text": format_deal_long(deal),
            "image_url": None,
            "alt": None,
        }
    )

    # Cierre
    closing = (
        "💡 Tip: Guarda este deal si encaja en tu stack.\n"
        "#SaaS #Deals #Productividad"
    )
    parts.append(
        {
            "text": closing,
            "image_url": None,
            "alt": None,
        }
    )

    return parts


def build_single_post_for_deal(deal, short: bool = False):
    return format_deal_short(deal) if short else format_deal_long(deal)
