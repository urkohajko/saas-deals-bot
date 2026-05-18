import os
from atproto import Client

def post_to_bluesky(text):
    username = os.getenv("BSKY_USERNAME")
    password = os.getenv("BSKY_APP_PASSWORD")

    client = Client()
    client.login(username, password)
    client.send_post(text)

if __name__ == "__main__":
    post_to_bluesky("Oferta SaaS del día 🚀")
