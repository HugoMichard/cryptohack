from pwn import xor
cryptohex = "63727970746f7b"
message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
key = bytes.fromhex("6d79584f526b6579")
print(xor(message, key))
