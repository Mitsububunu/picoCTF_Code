from struct import unpack, pack

# https://gist.github.com/c633/a7a5cde5ce1b679d3c0a
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

data = 'b1d3324cfce6ef5eede466cd57f5e17fcd7f55f6e964e7c97f75e954e64df779fcfc5171f93e18d900'.decode('hex')
data = data[:-1]


for i in range(len(data)-3-1, -1, -1):
  v, = unpack('<I', data[i:i+4])
  data = data[:i] + pack('<I', ror(v, 15, 4*8)) + data[i+4:]

  v, = unpack('<H', data[i:i+2])
  data = data[:i] + pack('<H', rol(v, 13, 2*8)) + data[i+2:]
  
  v, = unpack('<B', data[i:i+1])
  data = data[:i] + pack('<B', v ^ 0xde) + data[i+1:]

print data # picoCTF{gEt_y0Ur_sH1fT5_r1gHt_0cb381c60}