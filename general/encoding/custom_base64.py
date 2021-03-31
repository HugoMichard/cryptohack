import base64
from hex import convert_hex_to_bytes


def convert_bytes_to_base64(message):
    return base64.b64encode(message)


if __name__ == '__main__':
    flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    print(convert_bytes_to_base64(convert_hex_to_bytes(flag)))