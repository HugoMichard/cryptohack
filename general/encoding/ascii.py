def convert_to_ascii(message):
    r = ""
    for el in message:
        r += chr(el)
    return r


if __name__ == '__main__':
    flag = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    print(convert_to_ascii(flag))
