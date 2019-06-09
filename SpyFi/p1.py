def part_msg(message,part_length=16):
	sl=len(message)
	pl=part_length 
	m=[message[pl*i:min(sl,pl*i+pl)] for i in range(sl/pl+(sl%pl>0))]
	return m
msg=['Agent,\nGreetings. My situation report is as follows:\n','\nMy agent identifying code is: ','.\nDown with the Soviets,\n006\n',]

from pwn import connect
import string
import time
def solve():
	cnt=0
	flag='picoCTF{@'
	# sitrep,agent_code='',''
	# message =msg[0] +sitrep+msg[1]+agent_code+msg[2]
	for j in range(38-len(flag)):
		for i in string.printable:
			# print "flag:",i
			r=connect("2018shell.picoctf.com", 31123)
			cnt+=1;time.sleep(1)
			prompt=r.recvuntil("report: ")
			# 113 + (11+16+38+10)  + 38 = 226
			base='fying code is: '+flag
			sitrep='@'*11+base[-15:]+i+'@'*(38-len(flag)+10)
			# agent_code="#"*38
			# message =msg[0] +sitrep+msg[1]+agent_code+msg[2]
			# print '\n'.join(map(repr,part_msg(message)))
			r.sendline(sitrep)
			response=r.recv()
			# print len(response)
			tmp=part_msg(response,32)
			# print len(tmp)
			# print '\n'.join(tmp)
			r.close()
			# print len(msg[0]+sitrep+msg[1]+flag)/16
			if tmp[4]==tmp[len(msg[0]+sitrep+msg[1]+flag)/16]:
				flag+=i
				break
		print "flag:",flag,cnt

print "flag:",time.asctime()
solve()
print "flag:",time.asctime()