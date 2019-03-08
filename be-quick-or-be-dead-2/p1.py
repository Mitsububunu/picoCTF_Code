#!usr/bin/env python

from pwn import *

elf = ELF('./be-quick-or-be-dead-2')

#for key, address in elf.symbols.iteritems():
#    print key, hex(address)

#number = 57469627516743452992949879757918551298805560681917001257361517578717419486220126829288007778488491093655552360257511701831080084667270396068511122653792921071981072017637796336085787018434208569927808364391532229656984129
number = 13519797236961659458

elf.asm(elf.symbols['alarm'], 'ret')
elf.asm(elf.symbols['calculate_key'], 'mov eax, %s\nret\n' % (hex(number & 0xFFFFFFFF)))

elf.save('./new')
os.system('chmod +x ./new')

p = process('./new')
p.poll(True)
print p.recvall()