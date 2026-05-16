import threading
import time
from flask import Flask
from twitter_bot_selenium import TwitterBot

# Credenciales (puedes moverlas a variables de entorno si quieres)
TWITTER_USER = "TU_USUARIO"
TWITTER_PASS = "TU_PASSWORD"

app = Flask(__name__)

# -----------------------------
#   BOT THREAD
# -----------------------------
def run_bot():
    print("Starting SaaS Deals Bot...")

    try:
        bot = TwitterBot(TWITTER_USER, TWITTER_PASS)
        bot.login()

        while True:
            # Aquí puedes poner tu lógica real de publicación
            bot.tweet("🚀 SaaS Deals Bot funcionando correctamente en Render.")
            print("Tweet enviado. Esperando 1 hora...")
            time.sleep(3600)

    except Exception as e:
        print("Bot crashed:", e)

    finally:
        try:
            bot.close()
        except:
            pass


# -----------------------------
#   FLASK ROUTES
# -----------------------------
@app.route("/")
def home():
    return "SaaS Deals Bot Running"


# -----------------------------
#   MAIN ENTRYPOINT
# -----------------------------
if __name__ == "__main__":
    # Lanzar bot en un hilo separado
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()

    print("Flask server running on port 10000...")
    app.run(host="0.0.0.0", port=10000)
