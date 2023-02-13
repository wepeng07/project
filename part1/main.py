
# import sys, os
# sys.path.insert(1, os.path.join(os.getcwd(), 'part1'))
from crypt.rsa import Rsa
from mymath.mymath import hash
import random as rd


msg = 'Top secret message'
rsa = Rsa(rd.randint(500,1000))
print(hash(msg))
c, e = rsa.encrypt(hash(msg))
print(c,e)
print(rsa.decrypt(c, e))
print('Done')

# m = 65
# p = 61
# q = 53
# # rsa = Rsa(rd.randint(p,q))
# rsa = Rsa(p,q)

# c, e = rsa.encrypt(m)
# print(c,e)
# print(rsa.decrypt(c, e))
# print('Done')