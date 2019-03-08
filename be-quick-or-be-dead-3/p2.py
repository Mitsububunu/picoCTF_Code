import ctypes
inp = 0x19965
memo = {}
def calc(n):
    if n in memo:
        return memo[n]
    if n > 4:
        result = calc(n - 3) - calc(n - 4) + (calc(n - 1) - calc(n - 2)) + 4660 * calc(n - 5)
    else:
        result = n ** 2 + 9029
    memo[n] = result
    return result
for i in range(inp):
    calc(i)
print(ctypes.c_uint32(calc(inp)).value)
