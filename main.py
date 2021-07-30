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


def byte2int(b1, b2):
    int_list = []
    for b in [b1, b2]:
        if b in hexadecimal_dict.keys():
            int_list.append(hexadecimal_dict[b])
        else:
            int_list.append(int(b))

    return int_list[0]*16 + int_list[1]


## make UTF-8 into int
def encode_en_ja(string):
    byte_code = str(string.encode("UTF-8"))[2:-1]        ## [2:-1] remove b"..."

    encoded_list = []
    skip = 0
    for i, b in enumerate(byte_code):
        if skip:
            skip -= 1
            continue

        if (len(byte_code)-i) > 1:      ## avoid out of range at 38 below
            ## if not en
            if (b == "\\") & (byte_code[i+1] == "x"):       ## e.g. \x93
                encoded_list.append(byte2int(byte_code[i+2], byte_code[i+3]))
                skip = 3        ## e.g. skip x,9,3

            ## if en
            else:
                encoded_list.append(ord(b))

    return encoded_list


if __name__ == '__main__':
    opponent = sys.stdin.readline().rstrip()
    sender = sys.stdin.readline().rstrip()

    message = generate_message.GenerateMessage(opponent).get_generated_message(sender)
    print(",".join(list(map(lambda x: str(x), encode_en_ja(message)))))      ## make string: "," as delimiter
