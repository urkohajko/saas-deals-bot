def format_deal(deal: dict) -> str:
    """
    Formatea un deal en texto listo para publicar.
    """
    if not deal:
        return "Hoy no hay deals disponibles."

    name = deal.get("name", "").strip()
    price = deal.get("price", "").strip()
    old_price = deal.get("old_price", "").strip()
    link = deal.get("link", "").strip()

    if not name:
        return "Hoy no hay deals disponibles."

    texto = f"🔥 {name}"

    if price:
        texto += f" — {price}"
    if old_price:
        texto += f" (antes {old_price})"

    if link:
        texto += f"\n🔗 {link}"

    return texto.strip()


def build_posts(deals: list[dict]) -> list[dict]:
    """
    Convierte deals en posts listos para publicar.
    """
    if not deals:
        return [{"text": "Hoy no hay deals disponibles.", "image": None}]

    posts = []
    for d in deals:
        posts.append({
            "text": format_deal(d),
            "image": d.get("image_url")
        })

    return posts
