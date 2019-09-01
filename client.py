from lib.ws import Websocket
import re
import threading
import os
import json


def ask_query_save():
    global queries
    query_str = input("Enter queries seperated by a comma\n")
    queries = re.findall(r",?(?:\s?)([A-Za-z0-9]*),?(?:\s?)", query_str)
    queries.remove("")

    sel = input("Would you like to save this search profile? (Y/N)\n")
    if sel == "y" or sel == "Y":
        name = input("Enter a name for this profile\n")
        if len(config["profiles"]) == 0:
            id = 0
        else:
            id = config["profiles"][-1]["id"] + 1
        profile = {"id": id, "name": name, "queries": queries}
        config["profiles"].append(profile)

        config_str = json.dumps(config)
        with open("config.json", "w") as f:
            f.write(config_str)


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


def ask_profile():
    global queries
    global ask

    sel = input("Would you like to use a saved profile? (Y/N)\n")

    if sel == "y" or sel == "Y":
        for profile in config["profiles"]:
            print(str(profile["id"] + 1) + ".", profile["name"])
        sel = input("Select profile\n")

        for profile in config["profiles"]:
            if str(profile["id"] + 1) == sel:
                queries = profile["queries"]
            else:
                continue
    elif sel == "n" or sel == "N":
        ask_query_save()


print("Path of Exile trade sniper 1.1")

if os.path.isfile("config.json") is False:
    setup()
else:
    config = read_config()
    config = json.loads(config)

if len(config["profiles"]) > 0:
    ask_profile()
else:
    ask_query_save()


threads = []
for query in queries:
    thread = threading.Thread(target=Websocket, args=(query, config["poesessid"]))
    threads.append(thread)
    thread.start()