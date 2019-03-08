import os
import mmap

BMP_HEADER_SIZE = 54
BITS_PER_BYTE = 8

def memory_map(filename, access=mmap.ACCESS_READ):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

with memory_map("pico2018-special-logo.bmp") as b:
    for i in range(BMP_HEADER_SIZE,
                   len(b) - BMP_HEADER_SIZE - BITS_PER_BYTE,
                   BITS_PER_BYTE):
        chunk = b[i:i+BITS_PER_BYTE]
        new_byte = 0
        for x, byte in enumerate(chunk):
            new_byte |= (byte & 0x01) << (BITS_PER_BYTE - x - 1)
        c = chr(new_byte)
        if new_byte == 0:
            break
        print (c, end='')