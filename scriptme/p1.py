from pwn import *

def get_depth(group):
    current_depth = 0
    max_depth = 0
    for c in group:
        if c == '(':
            current_depth += 1
            max_depth = max(current_depth, max_depth)
        elif c == ')':
            current_depth -= 1
    return max_depth

def solve(s):
    s = s.replace(" = ???", "").strip()
    groups = s.split(" + ")
    while len(groups) > 1:
        log.info("Handling elements 1+2 out of {}".format(len(groups)))
        group1 = groups.pop(0)
        group2 = groups.pop(0)
        #print "{}, {}".format(group1, group2)

        d1 = get_depth(group1)
        d2 = get_depth(group2)
        log.info("Depth1: {}, Depth2: {}".format(d1, d2))

        if d1 > d2:
            new_group = group1[:-1] + group2 + ')'
        elif d2 > d1:
            new_group = '(' + group1 + group2[1:]
        else:
            new_group = group1 + group2

        groups.insert(0, new_group)
        log.info("New element:\n{}".format(new_group))

    return groups[0]

r = remote("2018shell.picoctf.com", 7866)
r.recvuntil("warmup.")
while True:
    line = r.recvline_contains(["???", "pico"])
    log.info("Received:\n{}".format(line))
    if "pico" in line:
        break
    r.recvuntil("> ")
    answer = solve(line)
    log.info("Responded: \n{}".format(answer))
    
    r.sendline(answer)
    line = r.recvline()
    if not "Correct!" in line:
        print r.recvall()
        break