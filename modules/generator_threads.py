def generar_hilo_deal(deal: dict) -> list[str]:
    """
    Genera un hilo humano basado en un deal.
    """
    if not deal:
        return ["Hoy no hay deals disponibles."]

    name = deal.get("name", "").strip()
    price = deal.get("price", "").strip()
    old_price = deal.get("old_price", "").strip()
    link = deal.get("link", "").strip()

    partes = []

    partes.append(f"🔥 Nuevo deal SaaS: {name}")
    partes.append(f"💰 Precio actual: {price}")
    if old_price:
        partes.append(f"❌ Antes costaba: {old_price}")
    partes.append(f"🔗 Enlace: {link}")
    partes.append("💡 Más deals cada día en SaaS Deals.")

    return partes
