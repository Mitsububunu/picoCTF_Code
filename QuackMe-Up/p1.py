#!/usr/bin/env python

from pwn import *
import string


p = process('./main')

print p.recv()

alphabet = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

p.sendline(alphabet)

lines = p.recvall().split('\n')
log.info('lines: {}'.format(lines))

m = lines[0].split(':')[2].strip()
q = lines[1].split(':')[1].strip()

mm = { }
for a, c in zip(alphabet, m.split()):
	mm[c] = a

log.info('Map: {}'.format(m))
log.info('Need to decrypt: {}'.format(q))
log.info('mm: {}'.format(mm))

s = ''
for c in q.split():
	s += mm[c]

print s