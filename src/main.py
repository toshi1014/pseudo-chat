import sys
from web_socket.server import WebsocketServerDerived
from message_client import MessageClient
import threading

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDRESS = f"ws://{HOST}:{PORT}"
OPPONENT_NAME = sys.argv[3]

if __name__ == '__main__':
    server = threading.Thread(target=WebsocketServerDerived, args=(PORT, HOST))
    server.start()
    print("server launching...")
    client = threading.Thread(target=MessageClient, args=(ADDRESS, OPPONENT_NAME))
    client.start()
    print("client connecting...")
    print("\nsuccess")