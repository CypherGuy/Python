# main.py

from mafia_bot import MafiaBot


def main():
    bot = MafiaBot()
    bot.start()


if __name__ == "__main__":
    main()


# import sys
# import nltk
# import random
# import time
# import json
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium import webdriver
# from dotenv import load_dotenv
# import os
# import selenium.common.exceptions
# import datetime

# load_dotenv()

# # https://mafia.gg/api/users/{id}

# with open("types.json") as f:
#     rooms: dict = json.load(f)

# COMMAND = "\033[0;36m"
# RESET = "\033[0m"


# def seconds_to_hms():
#     return datetime.datetime.now().strftime("%H:%M:%S")


# def main():

#     link = input("Enter link to join: ")

#     # Add hosts here, case sensitive
#     allowedHosts = ['_Sip_', "Lagmaker", "getdropkicked"]
#     service = ChromeService()
#     driver = webdriver.Chrome(service=service)

#     driver.get("https://mafia.gg/login")
#     driver.maximize_window()

#     # Find the input box by its id
#     username = driver.find_element(
#         By.XPATH, "/html/body/div[1]/div/div/main/div/form/fieldset/div[1]/input")
#     username.send_keys("Despa1r")
#     password = driver.find_element(
#         By.XPATH, "/html/body/div[1]/div/div/main/div/form/fieldset/div[2]/input")
#     password.send_keys(os.getenv("PASSWORD"))
#     # Click the login button
#     login_button = driver.find_element(
#         By.XPATH, "/html/body/div[1]/div/div/main/div/form/fieldset/button/span[1]")
#     login_button.click()

#     if not link:
#         for i in range(1, 10):  # Rarely more then 3 lobbies
#             name = driver.find_element(
#                 By.XPATH, f"/html/body/div[1]/main/div/div[2]/div/div[1]/div/div[3]/a[{i}]/div/strong[1]")
#             if name.text in allowedHosts:
#                 name.click()  # Join lobby
#                 break
#     else:
#         driver.get(link)

#     driver.implicitly_wait(0.5)

#     start = time.time()

#     def getElements():
#         try:
#             chatbox = driver.find_element(
#                 By.CSS_SELECTOR, "body > div.main > main > div > div.game-center > div.game-chat-bar > form > input[type=text]")
#         except:
#             try:
#                 chatbox = driver.find_element(
#                     By.XPATH, "/html/body/div[1]/main/div/div[3]/div[3]/form/input")
#             except:
#                 chatbox = driver.find_element(
#                     By.TAG_NAME, "input")
#         sendButton = driver.find_element(
#             By.XPATH, "/html/body/div[1]/main/div/div[3]/div[3]/form/button/span[1]")

#         messageList = driver.find_elements(
#             By.CLASS_NAME, "game-chronicle-chat-1nner muted")

#         try:
#             readyButton = driver.find_element(
#                 By.CSS_SELECTOR, "body > div.main > main > div > div.game-left > div.game-action-panel > div > div.scrollable-inner > div > div > div > div > div > button")
#         except:
#             readyButton = None
#         return chatbox, sendButton, messageList, readyButton

#     chatbox, sendButton, messageList, readyButton = getElements()

#     startmsgcount = len(messageList)

#     cogs = {"checkdeath": True, "deads": [], "playered": False}

#     def seconds_to_hms(seconds):
#         hours = seconds // 3600
#         minutes = (seconds % 3600) // 60
#         seconds = seconds % 60
#         return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

#     commands = {
#         "help | commands": "Displays a list of commands",
#         "time": "Displays how long the bot has been up for",
#         "roles": "Displays a link to the roles page",
#         "repeat": "Repeats a message",
#         "ping": "Pong",
#         "ranroom <Players>": "Suggests a random room with an optional player count",
#         "randumbs": "Suggests a random room from the randumbs preset",
#         "getroom <Room name>": "Displays the code for a given room name",
#     }

#     def mainorspec():  # Is the bot in pregame or spectating?
#         messageList = driver.find_elements(
#             By.CLASS_NAME, "muted")
#         if len(messageList) < 2:
#             messageList = driver.find_elements(
#                 By.CLASS_NAME, "game-chronicle-chat-inner")
#         return messageList

#     while True:
#         try:
#             messageList = mainorspec()
#             print(len([i.text for i in messageList]))
#             # New message sent
#             if len(messageList) > startmsgcount and "Despa1r" not in messageList[-1].text:
#                 print(
#                     f"{COMMAND}[{seconds_to_hms()}]{RESET} {messageList[-1].text}")

#                 # Things to do when any message is sent

#                 if cogs["checkdeath"] == True:
#                     time.sleep(0.08)
#                     sysmessages = driver.find_elements(
#                         By.CLASS_NAME, "game-chronicle-sys-message-text")
#                     sysmessages = filter(
#                         lambda x: "died." in x.accessible_name, sysmessages)

#                     for i in sysmessages:
#                         if "died." in i.accessible_name:
#                             words = i.accessible_name.split(" ")
#                             name = words[-3]
#                             if name not in cogs["deads"]:
#                                 cogs["deads"].append(name)

#                                 chatbox.send_keys(
#                                     f"Welcome to the afterlife, {name}...")
#                                 sendButton.click()
#                                 break

#                 # Reactionary commands (to other people's messages)
#                     last_message = messageList[-1].text.lower()

#                     if "despair" in last_message or "despa1r" in last_message and not last_message.startswith("despa1r"):
#                         if last_message.startswith("hot655"):
#                             chatbox.send_keys(
#                                 "Hello Hot, it's Despair :D ")
#                         else:
#                             chatbox.send_keys(
#                                 "Despair? That must be me. What's up?")
#                         sendButton.click()

#                 # Private commands

#                 if messageList[-1].text.startswith(tuple(allowedHosts)):

#                     if "/help" in messageList[-1].text:
#                         chatbox.send_keys(
#                             f"Commands: {' ||| '.join([f'{i}: {commands[i]}' for i in commands])}"
#                         )
#                         sendButton.click()

#                     if "/fraudwatch" in messageList[-1].text:
#                         chatbox.send_keys(
#                             "List of frauds: Go and jo, Manchester United"
#                         )
#                         sendButton.click()

#                     if "/toggledeath" in messageList[-1].text:
#                         cogs["checkdeath"] = not cogs["checkdeath"]
#                         chatbox.send_keys("Should be inverted.")
#                         sendButton.click()

#                     elif "/suicide" in messageList[-1].text and messageList[-1].text.startswith("_Sip_"):
#                         chatbox.send_keys(
#                             f"Suiciding..")
#                         sendButton.click()
#                         sys.exit()

#                     elif "/allies" in messageList[-1].text and messageList[-1].text.startswith("_Sip_"):
#                         try:
#                             text = messageList[-1].text.split(" ", 1)[1]
#                             action, user = text.split(" ", 1)
#                             if action == "a":
#                                 try:
#                                     allowedHosts.append(user)
#                                     chatbox.send_keys(
#                                         f"Added {user} to allies")
#                                     sendButton.click()
#                                 except ValueError:
#                                     continue
#                             elif action == "r":
#                                 try:
#                                     allowedHosts.remove(user)
#                                     chatbox.send_keys(
#                                         f"Removed {user} from allies")
#                                     sendButton.click()
#                                 except ValueError:
#                                     continue

#                         except IndexError:
#                             chatbox.send_keys(
#                                 f"{' '.join(allowedHosts)}")
#                             sendButton.click()

#                     elif "/ready" in messageList[-1].text and messageList[-1].text.startswith("_Sip_") and cogs["playered"] == False:
#                         print("ready")
#                         if readyButton:
#                             try:
#                                 readyButton.click()
#                                 cogs["playered"] = True
#                                 chatbox.send_keys(
#                                     "I am a bot and I have readied up.")
#                                 sendButton.click()
#                             except:
#                                 chatbox.send_keys(
#                                     "Can't find the button")
#                                 sendButton.click()
#                         else:
#                             continue

#                     elif "/unready" in messageList[-1].text and messageList[-1].text.startswith("_Sip_") and cogs["playered"] == True:
#                         if readyButton:
#                             try:
#                                 readyButton.click()
#                                 cogs["playered"] = False
#                             except:
#                                 chatbox.send_keys(
#                                     "Couldn't find the ready button")
#                                 sendButton.click()
#                         else:
#                             chatbox.send_keys("Ready button? Can't find it")
#                             sendButton.click()

#                     elif "/time" in messageList[-1].text:
#                         end = time.time()
#                         chatbox.send_keys(
#                             f"I've been up for -> {seconds_to_hms(end-start)}")
#                         sendButton.click()

#                     elif "/roles" in messageList[-1].text:
#                         chatbox.send_keys(
#                             f"For a list of roles, refer to https://mafia.gg/guide/roles")
#                         sendButton.click()

#                     elif "/repeat" in messageList[-1].text:
#                         try:
#                             text = messageList[-1].text.split(" ", 1)[1]
#                         except IndexError:
#                             continue
#                         if text:
#                             chatbox.send_keys(text)
#                             sendButton.click()

#                     elif "/ping" in messageList[-1].text:
#                         print("Ping")
#                         chatbox.send_keys("Pong")
#                         sendButton.click()

#                     elif "/ranroom" in messageList[-1].text:
#                         print("Ranroom")
#                         try:
#                             # Amount of players given
#                             text = messageList[-1].text.split(" ", 1)[1]
#                             try:
#                                 if int(text) < 3 or int(text) > 25:
#                                     chatbox.send_keys(
#                                         "Please enter a number between 3 and 25")
#                                     sendButton.click()
#                                     continue
#                                 filteredRooms = filter(
#                                     lambda name: rooms["setups"][name]["players"] == text, rooms["setups"].keys())
#                                 filteredlist = list(filteredRooms)
#                                 randomroomname = random.choice(filteredlist)
#                                 chatbox.send_keys(
#                                     f"""Maybe try {randomroomname}! It has code {rooms['setups'][randomroomname]['code']} and requires {rooms['setups'][randomroomname]['players']} players. You can find out more at  https://mafiagg.fandom.com/wiki/{randomroomname.replace(' ', '_')}"""
#                                 )
#                                 sendButton.click()
#                             except ValueError:
#                                 continue

#                         except IndexError:  # No setup name given
#                             randomroomname = random.choice(
#                                 list(rooms["setups"].keys()))
#                             chatbox.send_keys(
#                                 f"""Maybe try {randomroomname}! It has code {rooms['setups'][randomroomname]['code']} and requires {rooms['setups'][randomroomname]['players']} players. You can find out more at https://mafiagg.fandom.com/wiki/{randomroomname.replace(' ', '_')}"""
#                             )
#                             sendButton.click()
#                     elif "/randumbs" in messageList[-1].text:
#                         try:
#                             randomroomname = random.choice(
#                                 (rooms["presets"]["randumbs"]))
#                             chatbox.send_keys(randomroomname)
#                             sendButton.click()
#                         except:
#                             continue

#                     elif "/getroom" in messageList[-1].text:
#                         param = messageList[-1].text.split(" ", 1)[1]
#                         try:
#                             code = rooms["setups"][param.title()]["code"]
#                         except KeyError:
#                             code = f"That setup isn't in my database, have a look here: https://mafiagg.fandom.com/wiki/{param.replace(' ', '_')}"
#                         chatbox.send_keys(code)
#                         sendButton.click()

#             time.sleep(0.3)  # Prevents spamming
#         except selenium.common.exceptions.StaleElementReferenceException:
#             chatbox, sendButton, messageList, _ = getElements()
#             continue


# if __name__ == "__main__":
#     main()

#     # To do:
#     # ---Give the bot a website link to join--- COMPLETE
#     # Store maf, town, 3p wins under a certain setup in order to view town/maf winrates
#     # Host lobbies
#     # Get user info


# """
# it could keep track of how many town / 3p / mafia wins there were in a given lobby
# or for a given setup so ppl can track whether theyre hosting townsided/mafsided games


# yeah you could share that with the /randsetup data

# """
