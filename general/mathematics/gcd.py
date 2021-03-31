def gcd(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


if __name__ == '__main__':
    a = 66528
    b = 52920
    print(gcd(a, b))
