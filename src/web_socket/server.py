from websocket_server import WebsocketServer

class WebsocketServerDerived(WebsocketServer):
    def __init__(self, port, host):
        super().__init__(port, host=host)
        self.run()

    def new_client(self, client, server):
        self.send_message_to_all("[server] new client has joined")

    def client_left(self, client, server):
        pass

    def message_received(self, client, server, message):
        self.send_message_to_all(message)

    def run(self):
        self.set_fn_new_client(self.new_client)
        self.set_fn_client_left(self.client_left)
        self.set_fn_message_received(self.message_received)
        self.run_forever()