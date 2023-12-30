import random
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

# https://mafia.gg/api/users/{id}

with open("types.json") as f:
    rooms: dict = json.load(f)


def main():

    link = input("Enter link to join: ")

    allowedHosts = ['_Sip_']  # Add hosts here, case sensitive
    service = ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(1)

    if not link:
        driver.get("https://mafia.gg/login")
    else:
        driver.get(link)
    driver.maximize_window()

    # Find the input box by its id
    username = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/main/div/form/fieldset/div[1]/input")
    username.send_keys("Despa1r")
    password = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/main/div/form/fieldset/div[2]/input")
    password.send_keys(os.getenv("PASSWORD"))
    # Click the login button
    login_button = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/main/div/form/fieldset/button/span[1]")
    login_button.click()

    if not link:
        for i in range(1, 10):  # Rarely more then 3 lobbies
            name = driver.find_element(
                By.XPATH, f"/html/body/div[1]/main/div/div[2]/div/div[1]/div/div[3]/a[{i}]/div/strong[1]")
            if name.text in allowedHosts:
                name.click()  # Join lobby
                break

    start = time.time()
    # As a check
    driver.get(link)
    time.sleep(3)

    chatbox = driver.find_element(
        By.XPATH, "/html/body/div[1]/main/div/div[3]/div[3]/form/input")
    sendButton = driver.find_element(
        By.XPATH, "/html/body/div[1]/main/div/div[3]/div[3]/form/button/span[1]")

    readyButton = driver.find_element(
        By.XPATH, "/html/body/div[1]/main/div/div[3]/div[3]/form/button")

    messageList = driver.find_elements(
        By.CLASS_NAME, "game-chronicle-chat-inner")

    startmsgcount = len(messageList)

    states = {"playered": False}

    def seconds_to_hms(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    while True:

        try:
            newgamelink = driver.find_element(
                By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[2]/a")
            newgamelink.click()
            print("-----------")
            print("New game started")
        except:
            pass

        messageList = driver.find_elements(
            By.CLASS_NAME, "game-chronicle-chat-inner")
        if len(messageList) > startmsgcount:  # New message sent
            print(messageList[-1].text)
            if messageList[-1].text.startswith(tuple(allowedHosts)):
                print(messageList[-1].text)
                if "/time" in messageList[-1].text:
                    end = time.time()
                    chatbox.send_keys(
                        f"I've been up for -> {seconds_to_hms(end-start)}")
                    sendButton.click()
                if "/roles" in messageList[-1].text:
                    end = time.time()
                    chatbox.send_keys(
                        f"For a list of roles, refer to https://mafia.gg/guide/roles")
                    sendButton.click()
                if "/ready" in messageList[-1].text and states["playered"] == False:
                    time.sleep(random.random())
                    readyButton.click()
                    states["playered"] = True
                if "/unready" in messageList[-1].text and states["playered"] == True:
                    time.sleep(random.random())
                    readyButton.click()
                    states["playered"] = False
                if "/repeat" in messageList[-1].text:
                    try:
                        text = messageList[-1].text.split(" ", 1)[1]
                    except IndexError:
                        continue
                    if text:
                        print(text)
                        chatbox.send_keys(text)
                        sendButton.click()
                if "/ping" in messageList[-1].text:
                    chatbox.send_keys("Pong")
                    sendButton.click()
                if "/ranroom" in messageList[-1].text:
                    try:
                        # Setup name given
                        text = messageList[-1].text.split(" ", 1)[1]
                        try:
                            if int(text) < 3 or int(text) > 25:
                                chatbox.send_keys(
                                    "Please enter a number between 3 and 25")
                                sendButton.click()
                                continue
                            filteredRooms = filter(
                                lambda name: rooms["setups"][name]["players"] == text, rooms["setups"].keys())
                            randomroomname = random.choice(list(filteredRooms))
                            chatbox.send_keys(
                                f"""Maybe try {randomroomname}! It has code {rooms['setups'][randomroomname]['code']} and requires {rooms['setups'][randomroomname]['players']} players. You can find out more at  https://mafiagg.fandom.com/wiki/{randomroomname.replace(' ', '_')}"""
                            )
                            sendButton.click()
                        except ValueError:
                            continue

                    except IndexError:  # No setup name given
                        randomroomname = random.choice(
                            list(rooms["setups"].keys()))
                        chatbox.send_keys(
                            f"""Maybe try {randomroomname}! It has code {rooms['setups'][randomroomname]['code']} and requires {rooms['setups'][randomroomname]['players']} players. You can find out more at https://mafiagg.fandom.com/wiki/{randomroomname.replace(' ', '_')}"""
                        )
                        sendButton.click()
                if "/randumbs" in messageList[-1].text:
                    try:
                        randomroomname = random.choice(
                            (rooms["presets"]["randumbs"]))
                        chatbox.send_keys(randomroomname)
                        sendButton.click()
                    except:
                        continue

        time.sleep(0.5)


if __name__ == "__main__":
    main()

    # To do:
    # Give the bot a website link to join
    # Host lobbies
    # Get user info
