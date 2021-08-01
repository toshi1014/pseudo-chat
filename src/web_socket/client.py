import websocket
import _thread as thread
import time


class WebsocketClient():
    def __init__(self, address):
        time.sleep(1)           ## wait for server launch
        self.ws = websocket.WebSocketApp(address,
            on_message=lambda ws, msg: self.on_message(ws, msg),
            on_close=lambda ws, msg: self.on_open(ws)
        )
        self.ws.on_open = lambda ws: self.on_open(ws)
        self.run_forever()

    def on_message(self, ws, message):
        pass

    def on_open(self, ws):
        self.ws.send("[py] connected successfully")

    def run_forever(self):
        self.ws.run_forever()