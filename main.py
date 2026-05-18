from atproto import Client
import os

username = os.getenv("BSKY_USERNAME")
password = os.getenv("BSKY_APP_PASSWORD")

client = Client()
client.login(username, password)

client.send_post("🔥 Oferta SaaS del día: mensaje de prueba automático")
