from pwn import xor

message = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")


for k in range(128):
    print(xor(message, k))