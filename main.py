import os
import tweepy
import time

API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

def post_deal(text):
    client.create_tweet(text=text)

print("Bot de SaaS Deals iniciado...")

while True:
    post_deal("🔥 Oferta SaaS del día: mensaje de prueba automático")
    print("Tweet enviado.")
    time.sleep(3600)
