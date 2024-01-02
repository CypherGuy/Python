# commands.py

import time
import sys
import random
from helper_functions import current_time, get_elements, find_ready_button, load_rooms, send_message

COMMAND = "\033[0;36m"
RESET = "\033[0m"

commands = {
    "help | commands": "Displays a list of commands",
    "time": "Displays how long the bot has been up for",
    "roles": "Displays a link to the roles page",
    "repeat": "Repeats a message",
    "ping": "Pong",
    "ranroom <Players>": "Suggests a random room with an optional player count",
    "randumbs": "Suggests a random room from the randumbs preset",
    "getroom <Room name>": "Displays the code for a given room name",
}


def process_commands(driver, message_list, cogs, allowed_hosts, commands, starttime):
    rooms = load_rooms("types.json")
    last_message = message_list[-1].text.lower()

    if "despair" in last_message or "despa1r" in last_message and not last_message.startswith("despa1r"):
        if last_message.startswith("hot655"):
            send_message(driver, "Hello Hot, it's Despair :D ")
        else:
            send_message(driver, "Despair? That must be me. What's up?")

    if message_list[-1].text.startswith(tuple(allowed_hosts)):
        if "/help" in last_message:
            send_message(
                driver, f"Commands: {' ||| '.join([f'{i}: {commands[i]}' for i in commands])}")

        elif "/fraudwatch" in last_message:
            send_message(
                driver, "List of frauds: Go and jo, Manchester United")

        elif "/toggledeath" in last_message:
            cogs["checkdeath"] = not cogs["checkdeath"]
            send_message(driver, "Should be inverted.")

        elif "/suicide" in last_message and last_message.startswith("_Sip_"):
            send_message(driver, "Suiciding..")
            sys.exit()

        elif "/allies" in last_message and last_message.startswith("_Sip_"):
            try:
                text = last_message.split(" ", 1)[1]
                action, user = text.split(" ", 1)
                if action == "a":
                    allowed_hosts.append(user)
                    send_message(driver, f"Added {user} to allies")
                elif action == "r":
                    allowed_hosts.remove(user)
                    send_message(driver, f"Removed {user} from allies")
            except IndexError:
                send_message(driver, ' '.join(allowed_hosts))

        elif "/unready" in last_message and last_message.startswith("_Sip_") and cogs["playered"]:
            if ready_button := find_ready_button(driver):
                try:
                    ready_button.click()
                    cogs["playered"] = False
                except:
                    send_message(driver, "Couldn't find the ready button")
            else:
                send_message(driver, "Ready button? Can't find it")

        elif "/time" in last_message:
            end = time.time()
            send_message(
                driver, f"I've been up for -> {current_time(end-starttime)}")

        elif "/roles" in last_message:
            send_message(
                driver, "For a list of roles, refer to https://mafia.gg/guide/roles")

        elif "/repeat" in last_message:
            try:
                text = last_message.split(" ", 1)[1]
                if text:
                    send_message(driver, text)
            except IndexError:
                pass  # Handle the IndexError as needed

        elif "/ping" in last_message:
            send_message(driver, "Pong")

        elif "/ranroom" in last_message:
            try:
                text = last_message.split(" ", 1)[1]
                try:
                    if int(text) < 3 or int(text) > 25:
                        send_message(
                            driver, "Please enter a number between 3 and 25")
                    filtered_rooms = filter(
                        lambda name: rooms["setups"][name]["players"] == text, rooms["setups"].keys())
                    filtered_list = list(filtered_rooms)
                    random_room_name = random.choice(filtered_list)
                    send_message(
                        driver, f"Maybe try {random_room_name}! It has code {rooms['setups'][random_room_name]['code']} and requires {rooms['setups'][random_room_name]['players']} players. You can find out more at  https://mafiagg.fandom.com/wiki/{random_room_name.replace(' ', '_')}")
                except ValueError:
                    send_message(driver, "Please enter a valid number")

            except IndexError:
                random_room_name = random.choice(list(rooms["setups"].keys()))
                send_message(
                    driver, f"Maybe try {random_room_name}! It has code {rooms['setups'][random_room_name]['code']} and requires {rooms['setups'][random_room_name]['players']} players. You can find out more at https://mafiagg.fandom.com/wiki/{random_room_name.replace(' ', '_')}")

        elif "/randumbs" in last_message:
            try:
                random_room_name = random.choice(rooms["presets"]["randumbs"])
                send_message(driver, random_room_name)
            except:
                pass  # Handle the exception as needed

        elif "/getroom" in last_message:
            try:
                param = last_message.split(" ", 1)[1]
                try:
                    code = rooms["setups"][param.title()]["code"]
                except KeyError:
                    code = f"That setup isn't in my database, have a look here: https://mafiagg.fandom.com/wiki/{param.replace(' ', '_')}"
                send_message(driver, code)
            except IndexError:
                code = f"There was an error, please try again."
                send_message(driver, code)
