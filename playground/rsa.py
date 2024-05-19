from random import randint

# choose prime numbers (p and q)
p, q = 17, 19


# calculating our modulus, n
n = p * q


# find number of positive integers coprime with n

def eulers_totient_function(p, q):
    return (p - 1) * (q - 1)
phi = eulers_totient_function(p, q)


# let us build a function that calculates the greatest common
# divisor using the long division method

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a


# generate a public exponent for encrypting messages, e
# we'll check for random numbers less than phi that share a gcd of
# 1 with phi
e = randint(2, phi - 1)
while gcd(e, phi) != 1:
    e = randint(2, phi - 1)


# generate a private exponent for decrypting messages, d
# d is the modular multiplicative inverse, meaning that the modular
# exponentiation done with e is reversible using d
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1
d = mod_inverse(e, phi)

print('Primes', p, q)
print('Modulus:', n)
print('phi(n):', phi)
print('public:', e)
print('private:', d)

# text = input('Message:\n')
text = 'test'
ordinals = [ord(char) for char in text]
print(ordinals)
encrypted = [pow(ord(char), e, n) for char in text]
print(encrypted)
decrypted = ''.join([chr(pow(char, d, n)) for char in encrypted])
# decrypted = [pow(char,d,n) for char in encrypted]
print(decrypted)