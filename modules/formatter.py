# formatter.py
# Formatea un deal en texto listo para Bluesky

def format_deal(deal):
    name = deal["name"]
    price = deal["price"]
    old = deal["old_price"]
    link = deal["link"]

    return (
        f"🔥 {name}\n"
        f"💸 Antes: {old}\n"
        f"✅ Ahora: {price}\n\n"
        f"🔗 {link}\n"
        f"#SaaS #Deals #Ofertas"
    )
