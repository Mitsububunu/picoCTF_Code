from pwn import *
import re

host, port = '2018shell.picoctf.com', 15853

s = remote(host, port)
#------------------------------------------
prompt = s.recv()
print prompt

binary = re.findall('the (.*) as a word', prompt)[0]
answer = hex(int(binary.replace(' ', ''), 2))[2:].decode('hex')

s.sendline(answer)

#--------------------------------------------
prompt = s.recv()
print prompt

hexadecimal = re.findall('the (.*) as a word', prompt)[0]
answer = hexadecimal.decode('hex')

s.sendline(answer)

#--------------------------------------------
prompt = s.recv()
print prompt

octal = re.findall('the (.*) as a word', prompt)[0]
answer = ''.join([ chr(int(x,8)) for x in octal.split() ])

s.sendline(answer)


prompt = s.recv()
print prompt

s.close()