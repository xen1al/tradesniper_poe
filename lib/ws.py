import websocket


class Websocket:
    def __init__(self, query, cookie, league):
        self.query = query
        url = "wss://www.pathofexile.com/api/trade/live/{}/{}".format(league, query)
        headers = {"Cookie": cookie, "User-Agent": "tradesniper_poe"}

        print("INFO: Requesting websocket handhake for {}".format(query))
        socket = websocket.WebSocketApp(url, header=headers, on_message=self.message_handler)
        socket.run_forever()

    def message_handler(self, messages):
        pass
