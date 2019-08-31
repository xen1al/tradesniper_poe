import websocket
from lib.listing import Listing
import json
import pyperclip
from pynput import keyboard


class Websocket:
    def __init__(self, query, cookie):
        self.query = query
        url = "wss://www.pathofexile.com/api/trade/live/Legion/{}".format(query)
        headers = {"Cookie": cookie}

        print("INFO: Requesting websocket handhake for {}".format(query))
        socket = websocket.WebSocketApp(url, header=headers, on_message=self.message_handler)
        socket.run_forever()

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

        print(listing.ign + ":", str(socket_count) + "S" + str(link_count) + "L", listing.itemName, listing.itemTypeLine, "for", listing.price, listing.currency, "in", listing.league)
        pyperclip.copy(listing.whisper)
        keyboard.Controller().press(keyboard.Key.f2)
        keyboard.Controller().release(keyboard.Key.f2)
