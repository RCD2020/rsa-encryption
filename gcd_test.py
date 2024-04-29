def gcd(a, b):
    while b != 0:
        print(f'a({a}), b({b}) = b({b}), a % b ({a % b})')
        a, b = b, a % b
    return a


if __name__ == '__main__':
    print(gcd(65,24))