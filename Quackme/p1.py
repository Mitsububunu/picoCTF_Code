import pwn

greeting_masseage = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"

xor_string = '\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x50\x14\x5d\x00\x19\x17\x59\x52\x5d\x00'

print pwn.xor(greeting_masseage, xor_string)