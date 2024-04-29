import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(num, accuracy=5):
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
        a = random.randrange(2, num - 1)
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

def generate_keypair(bit_length=1024):
    p = random.randint(2**(bit_length-1), 2**bit_length)
    while not is_prime(p):
        p = random.randint(2**(bit_length-1), 2**bit_length)

    q = random.randint(2**(bit_length-1), 2**bit_length)
    while not is_prime(q) or q == p:
        q = random.randint(2**(bit_length-1), 2**bit_length)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_msg

def decrypt(private_key, encrypted_msg):
    d, n = private_key
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in encrypted_msg])
    return decrypted_msg

def main():
    print("Generating RSA key pair...")
    public_key, private_key = generate_keypair()

    message = input("Enter message to encrypt: ")

    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)
    print(encrypted_message[0] == encrypted_message[3])

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
