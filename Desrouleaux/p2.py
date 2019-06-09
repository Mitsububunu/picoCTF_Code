import socket
import re
import json

HOSTNAME = "2018shell.picoctf.com"
PORTNUM = 10493
 
class Netcat:
    """ Python 'netcat like' module """
    def __init__(self, ip, port):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))
    def read(self, length = 1024):
        """ Read 1024 bytes off the socket """
        return self.socket.recv(length).decode()
    def read_until(self, data):
        """ Read data into the buffer until we have data """
        while not data in self.buff:
            self.buff += self.socket.recv(1024).decode()
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
        return rval
    def write(self, data):
        self.socket.send(data.encode())
    def close(self):
        self.socket.close()

FILEPATH = "incidents.json"
with open(FILEPATH) as f:
    buf = f.read()
json_dict = json.loads(buf)

ticket_num_by_src = {}
for t in json_dict["tickets"]:
    if t["src_ip"] in ticket_num_by_src:
        ticket_num_by_src[t["src_ip"]] += 1
    else:
        ticket_num_by_src[t["src_ip"]] = 1
sorted(ticket_num_by_src.items(), key=lambda x: x[1])

unique_dst_by_file = {}
for t in json_dict["tickets"]:
    if t["file_hash"] in unique_dst_by_file:
        if t["dst_ip"] not in unique_dst_by_file[t["file_hash"]]:
            unique_dst_by_file[t["file_hash"]] += [t["dst_ip"]]
    else:
        unique_dst_by_file[t["file_hash"]] = [t["dst_ip"]]
cnt = 0
for v in unique_dst_by_file.values():
    cnt += len(v)
avg_unique_dst_ip = cnt/len(unique_dst_by_file)

nc = Netcat(HOSTNAME, PORTNUM)

# You'll need to consult the file `incidents.json` to answer the following questions.
#
# What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.
msg = nc.read_until('you may give any of the most common ones.')
nc.write(list(ticket_num_by_src.keys())[0] + "\n")

# How many unique destination IP addresses were targeted by the source IP address 189.229.254.207?
msg = nc.read_until('by the source IP address ')
expr = nc.read_until('?')
m = re.match(r'(\d+\.\d+\.\d+\.\d+)', expr)
src_ipaddr = m.group(1)
nc.write(str(ticket_num_by_src[src_ipaddr]) + "\n")

# What is the number of unique destination ips a file is sent, on average? Needs to be correct to 2 decimal places.
msg = nc.read_until('Needs to be correct to 2 decimal places.')
nc.write("{:.2f}".format(avg_unique_dst_ip) + "\n")
print(nc.read())

nc.close()