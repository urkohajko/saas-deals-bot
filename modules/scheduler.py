import time
import traceback
from main import main

INTERVAL_HOURS = 6  # Ejecutar cada 6 horas

def run_scheduler():
    while True:
        try:
            print(">>> Ejecutando bot SaaS Deals...")
            main()
            print(">>> Ejecución completada.")
        except Exception as e:
            print("ERROR en ejecución del bot:")
            print(e)
            traceback.print_exc()

        # Esperar X horas
        time.sleep(INTERVAL_HOURS * 3600)


if __name__ == "__main__":
    run_scheduler()
