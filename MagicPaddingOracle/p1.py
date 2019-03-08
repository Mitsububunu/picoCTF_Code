#!/usr/bin/env python3

from binascii import unhexlify, hexlify
import socket 
import time

def until(sock, delim):
    if type(delim) == str:
        delim = delim.encode('utf-8')

    out = bytearray()
    while delim not in out:
        c = sock.recv(512)
        if len(c) == 0:
            raise Exception()
        out.extend(c)

    return out

def oracle(s):
    if type(s) == str:
        s = s.encode('utf-8')

    while True:
        try:
            with socket.socket() as sock:
                sock.connect(('2018shell.picoctf.com', 45008))
    
                until(sock, '?\n')
                sock.sendall(s + b'\n')
                get = until(sock, '\n')
    
                return b'invalid padding' not in get

        except Exception as e:
            time.sleep(0.1)
            continue

def decrypt(block):
    known = 0
    prev = bytearray(16)

    while known < 16:
        print(hexlify(prev))
        if not oracle(hexlify(prev+block)):
            prev[-known-1] = (prev[-known-1] + 1)%256
            continue

        known += 1
        print(known, hexlify(prev))

        for i in range(known):
            prev[-i-1] ^= (known+1)^known

    for i, v in enumerate(prev):
        prev[i] ^= 17
    return prev

sample = 'a214910447773be343b38a37eb11ede0de2055dc137ac626c625706299c4f269a2ee6aae3019c33f855857f96c47138ca38c0bdc2096d29e0d539cc8de071881910fe712a50bde2be6dd9cd00c45a3'
sample = unhexlify(sample)

target = '{"username": "admin", "expires": "3000-01-01", "is_admin": "true"}'
target += chr(-len(target)%16)*(-len(target)%16)
target = target.encode('utf-8')

out = bytearray(16)
for i in range(len(target)//16):
    want = target[-16*(i+1):][:16]
    cur = decrypt(out[:16])
    iv = bytearray([a^b for a,b in zip(want, cur)])
    iv.extend(out)
    out = iv
    print(hexlify(out))

print(hexlify(out))