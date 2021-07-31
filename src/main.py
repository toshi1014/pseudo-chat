import glob, sys
from core import *
from web_socket.server import WebsocketServerDerived
from message_client import MessageClient
import threading

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDRESS = f"ws://{HOST}:{PORT}"

if __name__ == '__main__':
    server = threading.Thread(target=WebsocketServerDerived, args=(PORT, HOST))
    server.start()
    print("server launched successfully")
    client = threading.Thread(target=MessageClient, args=([ADDRESS]))
    client.start()
    print("client connected successfully")