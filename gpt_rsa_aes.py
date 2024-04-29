import random
import math
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

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

def encrypt_rsa(public_key, plaintext):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_msg

def decrypt_rsa(private_key, encrypted_msg):
    d, n = private_key
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in encrypted_msg])
    return decrypted_msg

def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    return nonce, ciphertext, tag

def decrypt_aes(key, nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()

def main():
    print("Generating RSA key pair...")
    public_key, private_key = generate_keypair()

    message = input("Enter message to encrypt: ")

    # Generate AES symmetric key
    aes_key = get_random_bytes(16)

    # Encrypt message with AES
    nonce, ciphertext, tag = encrypt_aes(aes_key, message)

    # Encrypt AES key with RSA public key
    encrypted_aes_key = encrypt_rsa(public_key, aes_key.decode())

    print("Encrypted AES key:", encrypted_aes_key)
    print("AES nonce:", nonce)
    print("AES ciphertext:", ciphertext)
    print("AES tag:", tag)

    # Decrypt AES key with RSA private key
    decrypted_aes_key = decrypt_rsa(private_key, encrypted_aes_key)

    # Decrypt message with AES
    decrypted_message = decrypt_aes(decrypted_aes_key.encode(), nonce, ciphertext, tag)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
