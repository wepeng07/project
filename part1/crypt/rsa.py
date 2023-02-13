# from cmath import e
# from operator import mod
# import random as rd
# from re import S, X
# from socket import MsgFlag
# from this import s
# from tkinter import N
import random as rd

import sys
import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append('C:\\Users\\xuan\\Documents\\GitHub\\cise337-hw1-wepeng07')
sys.path.append("/home/runner/work/cise337-hw1-wepeng07/cise337-hw1-wepeng07")

from part1.mymath.mymath import isPrime, lcm, prikExp, pubkExp, modular_pow
# import the mymath module here.

class Rsa:
    # initialize to set p, q, and n.
    def __init__(self, X):
    # def __init__(self, p, q):
        
        prime_cnt = 0
        pq=[]
        for i in range(X, X + 1000):
            if isPrime(i):
                pq.append(i)
                prime_cnt += 1
                if (prime_cnt == 2):
                    break
        
        p = pq[0]
        q = pq[1]

        self.n =  p * q
        self.K = lcm(p - 1, q - 1)
        # print(self.K)
        
    

    # generates a cipher string for a message m
    def encrypt(self, hash_value):
        
        try:
            public_key_e = pubkExp(self.K)
        except -1:
            print("public_key get -1")

        print("public_key=", public_key_e)
        
        ciphertext_c = modular_pow(hash_value, public_key_e, self.n)

        return ciphertext_c, public_key_e
        
    # decrypts a cipher string to get back original message
    def decrypt(self, ciphertext_c, public_key_e):
        private_key_d = prikExp(public_key_e, self.K)
        print("private_key=", private_key_d)
        org_hash_value = modular_pow(ciphertext_c, private_key_d, self.n)
        print ("org_hash_value=", org_hash_value)
        return org_hash_value
        








    # self.p = p
        # self.q = q
        # n = p*q
        # self.n=n
        # print(self.K)
        



# , hash_value

        # public_key_e = 17    
        # print(public_key_e)
        # print("p q", self.p, self.q)
        # hash_value = hash(self)
        # print(self.n)
        # print(hash_value)
        # print()
        # print(ciphertext_c, public_key_e)