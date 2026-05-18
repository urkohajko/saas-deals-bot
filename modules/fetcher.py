import requests
from bs4 import BeautifulSoup


BASE_URL = "https://saasdeals.com/deals"  # Sustituye por tu URL real


def get_deals():
    """
    Scraping básico de ejemplo.
    Adáptalo a la estructura real de tu página.
    Devuelve lista de dicts:
    {
        "name": str,
        "price": str,
        "old_price": str,
        "link": str,
        "image_url": str | None
    }
    """
    try:
        resp = requests.get(BASE_URL, timeout=10)
        resp.raise_for_status()
    except Exception:
        # Fallback si falla el scraping
        return [
            {
                "name": "SaaS Premium",
                "price": "$29",
                "old_price": "$99",
                "link": "https://saasdeals.com/premium",
                "image_url": None,
            }
        ]

    soup = BeautifulSoup(resp.text, "html.parser")

    deals = []

    # EJEMPLO de estructura. Cambia los selectores a tu HTML real.
    cards = soup.select(".deal-card")
    for card in cards:
        name = (card.select_one(".deal-title") or {}).get_text(strip=True) if card.select_one(".deal-title") else None
        price = (card.select_one(".deal-price") or {}).get_text(strip=True) if card.select_one(".deal-price") else None
        old_price = (card.select_one(".deal-old-price") or {}).get_text(strip=True) if card.select_one(".deal-old-price") else None
        link_tag = card.select_one("a")
        link = link_tag["href"] if link_tag and link_tag.has_attr("href") else BASE_URL
        img_tag = card.select_one("img")
        image_url = img_tag["src"] if img_tag and img_tag.has_attr("src") else None

        if not name or not price:
            continue

        deals.append(
            {
                "name": name,
                "price": price,
                "old_price": old_price or "",
                "link": link,
                "image_url": image_url,
            }
        )

    if not deals:
        # Fallback si el HTML no coincide
        return [
            {
                "name": "SaaS Premium",
                "price": "$29",
                "old_price": "$99",
                "link": "https://saasdeals.com/premium",
                "image_url": None,
            }
        ]

    return deals
