from lib.ws import Websocket
import re
import threading
import os

print("Path of Exile trade sniper 1.0")
query_str = input("Enter queries seperated by a comma\n")
queries = re.findall(r",?(?:\s?)([A-Za-z0-9]*),?(?:\s?)", query_str)
queries.remove("")

if os.path.isfile("POESESSID") is False:
    global poesessid
    poesessid = input("Enter POESESSID\n")
    with open("POESESSID", "w") as f:
        f.write(poesessid)
else:
    with open("POESESSID", "r") as f:
        poesessid = f.read()


threads = []
for query in queries:
    thread = threading.Thread(target=Websocket, args=(query, poesessid))
    threads.append(thread)
    thread.start()