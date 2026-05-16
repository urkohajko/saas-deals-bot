import os
import tweepy
import time

API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def post_deal(text):
    api.update_status(text)

print("Bot de SaaS Deals iniciado...")

while True:
    post_deal("🔥 Oferta SaaS del día: mensaje de prueba automático")
    print("Tweet enviado.")
    time.sleep(3600)
