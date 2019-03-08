def isValid(key):
  s = 0
  for i in range(len(key)-1):
    s += (o(key[i])+1)*(i+1)
  print s%0x24
  return s % 0x24 == o(key[len(key)-1])

def o(c):
  v = ord(c)
  if v > 0x2f and v <= 0x39:
    return v-0x30
  if v <= 0x40 or v > 0x5a:
    print 'wrong'
    exit()
  return v - 0x37

key = 'Z'*14+'A'+'L'
print isValid(key) # True
print key # ZZZZZZZZZZZZZZAL