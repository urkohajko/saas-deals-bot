from atproto import Client
import os

username = os.getenv("BSKY_USERNAME")
password = os.getenv("BSKY_APP_PASSWORD")

print("USERNAME:", username)
print("PASSWORD:", password)

client = Client()
client.login(username, password)
client.send_post("Test post")
