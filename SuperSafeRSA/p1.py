from __future__ import print_function
from pwn import *

# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

c = 3753884192387786346177975647750225500401305519088450619911941661957999643638216
n = 16778278943571944009683373840230362401865422190741249046222866179264633046760757

# calculation: https://www.alpertron.com.ar/ECM.HTM

p = 105364073459545483496269576491472828411 
#p = 110380683891444775871975228832971138237
q = 159240985970554385453780610127068518099087
#q = 124434296959920777019712641638067872701407

e = 65537

phi = (p-1)*(q-1)

d = modinv(e, phi)
m = pow(c, d, n)

flag = unhex(hex(m)[2:])

print('flag: {}'.format(flag))