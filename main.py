from atproto import Client
from fetcher import get_deals
from formatter import build_posts
from publisher import publicar_tweet, publicar_hilo

# ============================
# CONFIGURACIÓN
# ============================

HANDLE = "tu-handle.bsky.social"
PASSWORD = "tu-password"

# ============================
# MAIN
# ============================

def main():
    client = Client()
    client.login(HANDLE, PASSWORD)

    # 1. Obtener deals reales
    deals = get_deals()

    # 2. Convertirlos en posts listos
    posts = build_posts(deals)

    # 3. Si hay varios → hilo
    if len(posts) > 1:
        partes = [p["text"] for p in posts]
        publicar_hilo(client, partes)
        return

    # 4. Si solo hay uno → post simple
    first = posts[0]
    publicar_tweet(client, first["text"])


if __name__ == "__main__":
    main()
