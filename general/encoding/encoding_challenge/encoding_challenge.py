from pwn import *
import json
from cryptohack.general.encoding.hex import convert_hex_to_bytes
from cryptohack.general.encoding.ascii import convert_to_ascii
import base64
import codecs

r = remote('socket.cryptohack.org', 13377)


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decode_received_data(received):
    encoding = received["type"]
    encoded = received["encoded"]
    if encoding == "base64":  # works
        decoded = base64.b64decode(encoded).decode("utf-8")
    elif encoding == "hex":  # works
        decoded = convert_hex_to_bytes(encoded).decode("utf-8")
    elif encoding == "bigint":  # works
        decoded = bytes.fromhex(encoded[2:]).decode("utf-8")
    elif encoding == "utf-8":  # works
        decoded = convert_to_ascii(encoded)
    elif encoding == "rot13":  # works
        decoded = codecs.decode(encoded, 'rot_13')
    return decoded


received = json_recv()

for k in range(100):
    print("Received type: ", received["type"])
    print("Received encoded value: ", received["encoded"])
    decoded = decode_received_data(received)
    print("Decoded value : ", decoded)
    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

    received = json_recv()

print(received["flag"])
