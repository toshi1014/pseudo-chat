from web_socket.client import WebsocketClient
from core import *

class MessageClient(generate_message.GenerateMessage, WebsocketClient):
    def __init__(self, address, opponent_name_):
        self.opponent_name = opponent_name_
        super(MessageClient, self).__init__(self.opponent_name)
        super(generate_message.GenerateMessage, self).__init__(address)

    def on_message(self, ws, message_in):
        ## if incoming_message came from js
        if message_in[:4] == "[js]":
            if message_in[:8] == "[js]send":
                message_out = self.get_generated_message("me")
            elif message_in[:11] == "[js]receive":
                message_out = self.get_generated_message(self.opponent_name)
            self.ws.send("[py]" + message_out)