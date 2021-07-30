import glob, sys
from core import *
from handle_character_code import *


if __name__ == '__main__':
    encoded_opponent = sys.stdin.readline().rstrip()
    encoded_sender = sys.stdin.readline().rstrip()
    opponent = decode_uft8(encoded_opponent)
    sender = decode_uft8(encoded_sender)

    message = generate_message.GenerateMessage(opponent).get_generated_message(sender)
    print(",".join(list(map(lambda x: str(x), encode_utf8(message)))))      ## make string: "," as delimiter
