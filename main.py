from atproto import Client
from fetcher import get_deals
from formatter import build_posts
from publisher import publicar_tweet, publicar_hilo
from generator_threads import generar_hilo_deal

HANDLE = "tu-handle.bsky.social"
PASSWORD = "tu-password"


def main():
    client = Client()
    client.login(HANDLE, PASSWORD)

    deals = get_deals()
    posts = build_posts(deals)

    # Si hay varios deals → hilo
    if len(posts) > 1:
        partes = [p["text"] for p in posts]
        publicar_hilo(client, partes)
        return

    # Si hay uno → hilo bonito
    if len(posts) == 1:
        deal = deals[0] if deals else None
        hilo = generar_hilo_deal(deal)
        publicar_hilo(client, hilo)
        return

    # Si no hay nada → fallback limpio
    publicar_tweet(client, "Hoy no hay deals disponibles.")


if __name__ == "__main__":
    main()
