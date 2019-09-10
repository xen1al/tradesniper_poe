from lib.ws import Websocket
import re
import threading
import os
import json
import pyperclip
from pynput import keyboard
from lib.listing import Listing
import winsound


class WS(Websocket):
    def message_handler(self, messages):
        socket_count = ""
        link_count = ""
        messages = json.loads(messages)
        for message in messages["new"]:
            listing = Listing(message, self.query)
            if listing.itemSockets != "":
                socket_count = 0
                socket_groups = []

                for socket in listing.itemSockets:
                    socket_count += 1
                    socket_groups.append(socket["group"])

                freq_group = max(set(socket_groups), key=socket_groups.count)
                link_count = socket_count - (socket_count - socket_groups.count(freq_group))

        print("INFO:", listing.ign + ":", str(socket_count) + "S" + str(link_count) + "L", listing.itemName,
              listing.itemTypeLine, "for", listing.price, listing.currency, "in", listing.league)
        winsound.PlaySound("C:/Windows/Media/notify.wav", winsound.SND_ASYNC)
        pyperclip.copy(listing.whisper)
        keyboard.Controller().press(keyboard.Key.f2)
        keyboard.Controller().release(keyboard.Key.f2)


def write_config(str):
    with open("config.json", "w") as f:
        f.write(str)


def read_config():
    with open("config.json", "r") as f:
        return f.read()


def setup():
    global config
    config = dict()

    config["poesessid"] = input("Enter POESESSID\n")
    config["profiles"] = []
    config_str = json.dumps(config)

    write_config(config_str)


def get_profile(id):
    global config

    for profile in config["profiles"]:
        if int(profile["id"]) == int(id):
            return profile
        else:
            continue


def save_profile(name, league, queries):
    global config

    if len(config["profiles"]) == 0:
        id = 0
    else:
        id = config["profiles"][-1]["id"] + 1
    profile = {"id": id, "name": name, "queries": queries, "league": league}
    config["profiles"].append(profile)

    config_str = json.dumps(config)
    with open("config.json", "w") as f:
        f.write(config_str)


def start(queries, league):
    global config

    threads = []
    for query in queries:
        thread = threading.Thread(target=WS, args=(query, config["poesessid"], league))
        threads.append(thread)
        thread.start()


print("Path of Exile trade sniper 1.1.1")

if os.path.isfile("config.json") is False:
    setup()
else:
    config = read_config()
    config = json.loads(config)

if len(config["profiles"]) > 0:
    sel = input("Would you like to use a saved profile? (Y/N)\n")

    if sel == "y" or sel == "Y":
        for profile in config["profiles"]:
            print(str(profile["id"] + 1) + ".", profile["name"])
        sel = input("Select profile\n")

        profile = get_profile(int(sel) - 1)
        queries = profile["queries"]
        league = profile["league"]
        start(queries, league)
    elif sel == "n" or sel == "N":
        query_str = input("Enter queries seperated by a comma\n")
        queries = re.findall(r",?(?:\s?)([A-Za-z0-9]*),?(?:\s?)", query_str)
        queries.remove("")

        league = input("Enter league\n")

        sel = input("Would you like to save this search profile? (Y/N)\n")
        if sel == "y" or sel == "Y":
            name = input("Enter a name for this profile\n")
            save_profile(name, league, queries)
            start(queries, league)
        elif sel == "n" or sel == "N":
            start(queries, league)
else:
    query_str = input("Enter queries seperated by a comma\n")
    queries = re.findall(r",?(?:\s?)([A-Za-z0-9]*),?(?:\s?)", query_str)
    queries.remove("")

    league = input("Enter league\n")

    sel = input("Would you like to save this search profile? (Y/N)\n")
    if sel == "y" or sel == "Y":
        name = input("Enter a name for this profile\n")
        save_profile(name, league, queries)
        start(queries, league)
    elif sel == "n" or sel == "N":
        start(queries, league)
