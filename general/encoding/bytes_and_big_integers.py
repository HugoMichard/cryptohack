from Crypto.Util.number import long_to_bytes, bytes_to_long


def convert_long_to_bytes(message):
    return long_to_bytes(message)


if __name__ == '__main__':
    flag = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    print(convert_long_to_bytes(flag))
