from atproto import Client
import os
import requests
from modules.publisher import build_posts


def download_image(url: str) -> bytes | None:
    if not url:
        return None
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.content
    except Exception:
        return None


def run_bot():
    username = os.getenv("BSKY_USERNAME")
    password = os.getenv("BSKY_APP_PASSWORD")

    client = Client()
    client.login(username, password)

    posts = build_posts()  # lista de hilos

    for thread in posts:
        if not thread:
            continue

        # Primer post del hilo
        first = thread[0]
        embed = None

        if first.get("image_url"):
            img_bytes = download_image(first["image_url"])
            if img_bytes:
                blob = client.upload_blob(img_bytes)
                embed = client.models.AppBskyEmbedImages.Main(
                    images=[
                        client.models.AppBskyEmbedImages.Image(
                            image=blob.blob,
                            alt=first.get("alt", first["text"][:80]),
                        )
                    ]
                )

        root_post = client.send_post(first["text"], embed=embed)

        # Resto del hilo
        parent = root_post
        for part in thread[1:]:
            embed = None
            if part.get("image_url"):
                img_bytes = download_image(part["image_url"])
                if img_bytes:
                    blob = client.upload_blob(img_bytes)
                    embed = client.models.AppBskyEmbedImages.Main(
                        images=[
                            client.models.AppBskyEmbedImages.Image(
                                image=blob.blob,
                                alt=part.get("alt", part["text"][:80]),
                            )
                        ]
                    )

            parent = client.send_post(
                part["text"],
                embed=embed,
                reply_to=parent.uri,
            )


if __name__ == "__main__":
    run_bot()
