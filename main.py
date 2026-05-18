from atproto import Client
import os

def run_bot():
    username = os.getenv("BSKY_USERNAME")
    password = os.getenv("BSKY_APP_PASSWORD")

    client = Client()
    client.login(username, password)

    # Cargar contenido desde tu módulo real
    from modules.publisher import build_post

    post_text = build_post()
    client.send_post(post_text)

if __name__ == "__main__":
    run_bot()
