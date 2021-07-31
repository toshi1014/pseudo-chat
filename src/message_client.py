from web_socket.client import WebsocketClient

class MessageClient(WebsocketClient):
    def __init__(self, address):
        super().__init__(address)

    def on_message(self, ws, message):
        ## if message came from js
        if message[:4] == "[js]":
            self.ws.send("[py]" + message[4:] + "!!!")