import os
import platform
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


class TwitterBot:
    def __init__(self, user, password):
        self.user = user
        self.password = password

        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--window-size=1920,1080")

        system = platform.system()

        if system == "Windows":
            print("Running on Windows → using local ChromeDriver")
            # En Windows NO usamos rutas manuales
            self.driver = webdriver.Chrome(options=chrome_options)

        else:
            print("Running on Linux (Render) → using /usr/bin/chromedriver")
            chrome_options.add_argument("--headless=new")
            chrome_options.binary_location = "/usr/bin/google-chrome"

            service = Service("/usr/bin/chromedriver")
            self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.driver.set_page_load_timeout(30)


    def login(self):
        print("Navigating to Twitter login...")
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)

        # Campo usuario
        user_input = self.driver.find_element(By.TAG_NAME, "input")
        user_input.send_keys(self.user)
        user_input.send_keys(Keys.ENTER)
        time.sleep(3)

        # Campo contraseña
        pwd_input = self.driver.find_element(By.NAME, "password")
        pwd_input.send_keys(self.password)
        pwd_input.send_keys(Keys.ENTER)
        time.sleep(5)

        print("Logged in successfully.")


    def tweet(self, text):
        print("Posting tweet...")
        self.driver.get("https://twitter.com/compose/tweet")
        time.sleep(4)

        textarea = self.driver.find_element(By.CSS_SELECTOR, "div[role='textbox']")
        textarea.send_keys(text)
        time.sleep(1)

        textarea.send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(3)

        print("Tweet posted.")


    def close(self):
        print("Closing browser...")
        self.driver.quit()
