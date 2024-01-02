# helper_functions.py

import json
from selenium.webdriver.common.by import By


def load_rooms(file):
    with open(file) as f:
        return json.load(f)


def get_elements(driver):
    try:
        chatbox = driver.find_element(
            By.CSS_SELECTOR, "body > div.main > main > div > div.game-center > div.game-chat-bar > form > input[type=text]")
    except:
        try:
            chatbox = driver.find_element(
                By.XPATH, "/html/body/div[1]/main/div/div[3]/div[3]/form/input")
        except:
            chatbox = driver.find_element(By.TAG_NAME, "input")
    send_button = driver.find_element(
        By.XPATH, "/html/body/div[1]/main/div/div[3]/div[3]/form/button/span[1]")

    message_list = driver.find_elements(
        By.CLASS_NAME, "game-chronicle-chat-inner-muted")

    try:
        ready_button = driver.find_element(
            By.CSS_SELECTOR, "body > div.main > main > div > div.game-left > div.game-action-panel > div > div.scrollable-inner > div > div > div > div > div > button")
    except:
        ready_button = None

    return chatbox, send_button, message_list, ready_button


def find_ready_button(driver):
    try:
        ready_button = driver.find_element(
            By.CSS_SELECTOR, "body > div.main > main > div > div.game-left > div.game-action-panel > div > div.scrollable-inner > div > div > div > div > div > button")
        return ready_button
    except:
        return None


def current_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"


def send_message(driver, message):
    chatbox, send_button, _, _ = get_elements(driver)
    chatbox.send_keys(message)
    send_button.click()


def main_or_spec(driver):
    message_list = driver.find_elements(By.CLASS_NAME, "muted")
    if len(message_list) < 2:
        message_list = driver.find_elements(
            By.CLASS_NAME, "game-chronicle-chat-inner")
    return message_list
