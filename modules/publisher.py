from atproto import Client

def publicar_tweet(client: Client, texto: str):
    """
    Publica un post simple en Bluesky.
    """
    if not texto or not texto.strip():
        texto = "Hoy no hay contenido disponible."

    client.send_post(texto.strip())


def publicar_hilo(client: Client, partes: list[str]):
    """
    Publica un hilo (thread) en Bluesky.
    Cada parte es un post.
    """
    if not partes:
        client.send_post("Hoy no hay contenido disponible.")
        return

    parent = None
    for parte in partes:
        if not parte or not parte.strip():
            parte = "..."

        if parent is None:
            parent = client.send_post(parte.strip())
        else:
            parent = client.send_post(parte.strip(), reply_to=parent)
