import numpy as np

message = "label"
key = 13
bin_message = ' '.join(format(ord(x), 'b') for x in message)

message = message.encode('utf-8')

for el in message:
    print(chr(el ^ key))