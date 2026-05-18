from atproto import Client
import os
from modules.publisher import build_post

def run_bot():
    username = os.getenv("BSKY_USERNAME")
    password = os.getenv("BSKY_APP_PASSWORD")

    client = Client()
    client.login(username, password)

    post = build_post()
    client.send_post(post)

if __name__ == "__main__":
    run_bot()
