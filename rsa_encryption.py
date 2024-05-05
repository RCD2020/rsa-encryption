'''
Apr 29, 2024
'''

from math_encrypted import (generate_prime, random_coprime,
                            modular_inverse)


def generate_keys(bit_length:int=1024):
    """
    Returns (public, private, modulus)

    bit_length 1024-2048 recommended for real encryption
    """

    # choose prime numbers, p and q
    p, q = generate_prime(bit_length), generate_prime(bit_length)

    # calculate our modulus, n
    n = p * q

    # find number of positive numbers coprime with n, phi
    # we do this using Euler's Totient Function
    # (p - 1) * (q - 1)
    phi = (p - 1) * (q - 1)

    # generate a public exponent for encryption, e
    # check for random numbers that are coprime with phi
    # that is to say share a greatest common divisor of 1
    e = random_coprime(phi)

    # generate a private exponent for decryption, d
    # d is the modular multiplicative inverse, meaning that the
    # modular exponentiation done with e is reversible using d
    d = modular_inverse(e, phi)

    return (e, d, n)


def encrypt(data, public, modulus):
    return [pow(num, public, modulus) for num in data]


def encrypt_text(text, public, modulus):
    return encrypt([ord(char) for char in text], public, modulus)


def decrypt(data, private, modulus):
    return [pow(num, private, modulus) for num in data]


def decrypt_text(data, private, modulus):
    return ''.join([chr(num) for num in decrypt(data, private, modulus)])


if __name__ == '__main__':
    public, private, modulus = generate_keys(1024)
    print(public, private, modulus)
    data = encrypt_text('test', public, modulus)
    print(data)
    print(decrypt_text(data, private, modulus))
    