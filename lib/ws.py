import websocket


class Websocket:
    def __init__(self, query, cookie, league):
        self.query = query
        url = "wss://www.pathofexile.com/api/trade/live/{}/{}".format(league, query)
        headers = {"Cookie": cookie, "User-Agent": "tradesniper_poe"}

        print("INFO: Requesting websocket handhake for {}".format(query))
        socket = websocket.WebSocketApp(url, header=headers, on_message=self.message_handler, on_error=self.error_handler, on_close=self.on_close, on_open=self.on_open, on_ping=self.on_ping)
        socket.run_forever()

    def on_ping(self):
        print("INFO: Requesting websocket handhake for {}".format(self.query))

    def on_open(self):
        print("INFO: Websocket handshake succesful")

    def on_close(self):
        print("INFO: Websocket closed")

    def error_handler(self, e):
        print("ERROR:", e)

    def message_handler(self, messages):
        pass
