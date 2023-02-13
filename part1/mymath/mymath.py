# from cmath import e
# from operator import truediv
import random as rd
# from re import M
# from tempfile import tempdir
# from tkinter import E

def isPrime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return False        
        else:
            return True
    else:
        return False


def gcd(a,b):
    c = min(a,b)
    for i in range(1, c + 1):
        if ((a % i == 0) and (b % i == 0)):
            gcd_number = i
    return gcd_number

def lcm(a,b):
    c = max(a,b)
    while(True):
        if ((c % a == 0) and (c % b == 0)):
            lcm = c
            break
        c += 1
    return lcm
    

# Generates public key exponent
def pubkExp(k):
    for e in range(2, k):
        if(gcd(e,k)==1):
            return e
            

# Generate private key exponent
def prikExp(x, y):
    if x > y:
        x,y = y,x
    for d in range(1, y):
        if ((( x % y) * (d % y)) % y == 1):
            return d
    return -1
    

# Returns the hash of a string message. Sum of its ascii characters.
def hash(s):
    ascii_sum = 0
    for ch in s:
        ascii_sum = ascii_sum + (ord(ch))
    return ascii_sum
    
 # Optimized method to compute  Modular Exponentiation algorithm.
def modular_pow(base, exponent, modulus):
    if (modulus == 1) :
        return 0
    c = 1
    for e_prime in range (0, exponent):
        c = (c * base) % modulus
    return c       
    