import glob, sys
from core import *

hexadecimal_dict = {
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
}


def decode_uft8(byte_list):
    str_hex = ""

    for byte in byte_list.split(","):
        str_hex_tmp = str(hex(int(byte)))[2:]        ## e.g. 228 => e4
        str_hex += str_hex_tmp

    byte_code = bytes.fromhex(str_hex)
    return byte_code.decode("UTF-8")


def byte2int(b1, b2):
    int_list = []
    for b in [b1, b2]:
        if b in hexadecimal_dict.keys():
            int_list.append(hexadecimal_dict[b])
        else:
            int_list.append(int(b))

    return int_list[0]*16 + int_list[1]


## make UTF-8 into int      e.g. \0e4 => 228
def encode_utf8(string):
    byte_code = str(string.encode("UTF-8"))[2:-1]        ## [2:-1] remove b"..."

    encoded_list = []
    skip = 0
    for i, b in enumerate(byte_code):
        if skip:
            skip -= 1
            continue

        if (len(byte_code)-i) > 1:      ## avoid out of range at 38 below
            ## if not alphabet
            if (b == "\\") & (byte_code[i+1] == "x"):       ## e.g. \x93
                encoded_list.append(byte2int(byte_code[i+2], byte_code[i+3]))
                skip = 3        ## e.g. skip x,9,3

            ## if alphabet
            else:
                encoded_list.append(ord(b))

    return encoded_list


if __name__ == '__main__':
    encoded_opponent = sys.stdin.readline().rstrip()
    encoded_sender = sys.stdin.readline().rstrip()
    opponent = decode_uft8(encoded_opponent)
    sender = decode_uft8(encoded_sender)

    message = generate_message.GenerateMessage(opponent).get_generated_message(sender)
    print(",".join(list(map(lambda x: str(x), encode_utf8(message)))))      ## make string: "," as delimiter
