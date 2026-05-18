import requests
from bs4 import BeautifulSoup

BASE_URL = "https://saasdeals.app/deals"  # Ajusta a tu URL real


def get_deals():
    """
    Scraping robusto.
    Si falla → devuelve [] (NO fallback antiguo).
    """
    try:
        resp = requests.get(BASE_URL, timeout=10)
        resp.raise_for_status()
    except Exception:
        # No devolvemos un deal falso → así evitamos mensajes antiguos
        return []

    soup = BeautifulSoup(resp.text, "html.parser")

    deals = []

    # Ajusta estos selectores a tu HTML real
    cards = soup.select(".deal-card")
    for card in cards:
        name_el = card.select_one(".deal-title")
        price_el = card.select_one(".deal-price")
        old_price_el = card.select_one(".deal-old-price")
        link_el = card.select_one("a")
        img_el = card.select_one("img")

        if not name_el or not price_el:
            continue

        deals.append({
            "name": name_el.get_text(strip=True),
            "price": price_el.get_text(strip=True),
            "old_price": old_price_el.get_text(strip=True) if old_price_el else "",
            "link": link_el["href"] if link_el and link_el.has_attr("href") else BASE_URL,
            "image_url": img_el["src"] if img_el and img_el.has_attr("src") else None,
        })

    # Si no hay deals reales → devolvemos lista vacía
    return deals
