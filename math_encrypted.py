'''
Apr 26, 2024
'''

from random import randint, randrange


def is_prime(num: int, accuracy: int) -> bool:
    if num == 2 or num == 3:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    
    # Miller-Rabin primality test
    s = num - 1
    t = 0
    while s % 2 == 0:
        s //= 2
        t += 1
    for _ in range(accuracy):
        a = randrange(2, num - 1)
        x = pow(a, s, num)

        if x == 1 or x == num - 1:
            continue

        for _ in range(t - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True


def generate_prime(bit_length: int) -> int:
    accuracy = int((bit_length * .35) // 1)

    prime = randint(2 ** (bit_length - 1), 2 ** bit_length)
    while not is_prime(prime, accuracy):
        prime = randint(2**(bit_length-1), 2**bit_length)
    
    return prime


def gcd(a: int, b: int) -> int:
    # find gcd via long division method
    while b != 0:
        a, b = b, a % b

    return a


def random_coprime(num: int) -> int:
    # finds a coprime number by generating random numbers and
    # checking that the gcd is 1
    coprime = randint(2, num - 1)
    while gcd(coprime, num) != 1:
        coprime = randint(2, num - 1)

    return coprime


if __name__ == '__main__':
    print(generate_prime(40))