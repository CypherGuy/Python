# mafia_bot.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from dotenv import load_dotenv
import os
import selenium.common.exceptions

from helper_functions import detect_death, load_rooms, main_or_spec
from commands import process_commands

load_dotenv()

lists = load_rooms("types.json")
allowed_hosts = lists["whitelist"]["users"]
print(allowed_hosts)


class MafiaBot:
    def __init__(self):
        self.allowed_hosts = allowed_hosts
        self.service = ChromeService()
        self.driver = webdriver.Chrome(service=self.service)
        self.start_time = time.time()
        self.cogs = {"check_death": True, "deads": [], "playered": False}
        self.commands = {
            "help | commands": "Displays a list of commands",
            "time": "Displays how long the bot has been up for",
            "roles": "Displays a link to the roles page",
            "repeat": "Repeats a message",
            "ping": "Pong",
            "ranroom <Players>": "Suggests a random room with an optional player count",
            "randumbs": "Suggests a random room from the randumbs preset",
            "getroom <Room name>": "Displays the code for a given room name",
        }

    def start(self):
        link = input("Enter link to join: ")
        self.initialize_driver(link)
        self.run_bot()

    def initialize_driver(self, link):
        self.driver.get("https://mafia.gg/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.5)

        try:
            username = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div/main/div/form/fieldset/div[1]/input")
        except:
            username = self.driver.find_elements(
                By.ID, "id-1704168933763-1")
        username.send_keys(os.getenv("USERNAME"))
        try:
            password = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div/main/div/form/fieldset/div[2]/input")
        except:
            password = self.driver.find_elements(
                By.ID, "id-1704168933763-2")
        password.send_keys(os.getenv("PASSWORD"))

        login_button = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/main/div/form/fieldset/button/span[1]")
        login_button.click()

        if not link:
            self.join_lobby()
        else:
            self.driver.get(link)

        self.driver.implicitly_wait(0.5)

    def join_lobby(self):
        for i in range(1, 10):  # Rarely more than 3 lobbies
            name = self.driver.find_element(
                By.XPATH, f"/html/body/div[1]/main/div/div[2]/div/div[1]/div/div[3]/a[{i}]/div/strong[1]")
            if name.text in self.allowed_hosts:
                name.click()  # Join lobby
                break

    def run_bot(self):

        try:
            host = self.driver.find_element(
                By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/ul/li[1]")
            print(f"Host: {host.text}")
        except:
            print("Host not found")
            host = None

        # Add lobby host as ally so they can run "host" commands
        if host:
            self.allowed_hosts.append(host.text)

        while True:
            try:
                message_list = main_or_spec(self.driver)
                if len(message_list) > 0 and "Despa1r" not in message_list[-1].text:
                    # detect_death(self.driver, self.cogs)
                    process_commands(
                        self.driver, message_list, self.cogs, self.allowed_hosts, self.start_time, self.commands)

                    time.sleep(0.3)  # Prevents spamming

            except selenium.common.exceptions.StaleElementReferenceException:
                continue
