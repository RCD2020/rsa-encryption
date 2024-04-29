'''
Apr 26, 2024
'''

from random import randint, randrange


def is_prime(num, accuracy):
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


def generate_prime(bit_length):
    accuracy = (bit_length * .35) // 1

    prime = randint(2 ** (bit_length - 1), 2 ** bit_length)
    while not is_prime(prime):
        prime = randint(2**(bit_length-1), 2**bit_length)
    
    return prime
