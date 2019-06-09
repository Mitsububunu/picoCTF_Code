from pwn import *
log=[
    10900,10800,10850,11000,10800,10750,10800,10850,
    10900,11000,10800,10800,11000,10900,10700,10850,
    10800,10850,11000,11050,10650,10800,10700,11000,
    10900,10950,10950,10800,11000,11100,11900,13400,
    13800,13400,12000,11000,10800,10800,10700,10800,
    10800,11000,10900,11050,11800,13100,14600,16100,
    16600,16400,14400,12800,11800,11000,10950,10800,
    10800,10800,10800,10800,10900,10850,10850,10800,
    10800,11000,11000,11000,11400,11900,13000,14000,
    14800,15800,16200,15800,14700,13700,12200,12100,
    11100,11000,10900,10800,10700,11000,11000,10800,
    10900,10700,10900,10800,10750,10950,10900,10800
]

r=remote('2018shell2.picoctf.com',2245)
prompt=r.recvuntil('num_IPs')
data=r.recv()
nums=data.split()
print(prompt,'\n',nums)
group=len(nums)/4
res=[]
for i in range(group):
	t=nums[i*4+2].split(':')
	tt=int(t[0])*4+int(t[1])/15
	if int(nums[i*4+3])>log[tt]:
		res.append(nums[i*4])

r.sendline(' '.join(res))
print(' '.join(res),r.recv())
r.close()

# [x] Opening connection to 2018shell2.picoctf.com on port 39410
# [x] Opening connection to 2018shell2.picoctf.com on port 39410: Trying 18.224.157.204
# [+] Opening connection to 2018shell2.picoctf.com on port 39410: Done
# You'll need to consult the file `traffic.png` to answer the following questions.


# Which of these logs have significantly higher traffic than is usual for their time of day? You can see usual traffic on the attached plot. There may be multiple logs with higher than usual traffic, so answer all of them! Give your answer as a list of `log_ID` values separated by spaces. For example, if you want to answer that logs 2 and 7 are the ones with higher than usual traffic, type 2 7.
#     log_ID      time  num_IPs 
# ['0', '0', '01:00:00', '11637', '1', '1', '01:30:00', '11640', '2', '2', '02:45:00', '11616', '3', '3', '10:45:00', '9962', '4', '4', '10:45:00', '10409', '5', '5', '11:45:00', '12732', '6', '6', '14:15:00', '10538', '7', '7', '16:15:00', '10233', '8', '8', '17:30:00', '10839', '9', '9', '20:15:00', '11936', '10', '10', '20:30:00', '9898', '11', '11', '21:45:00', '9653', '12', '12', '22:30:00', '10252', '13', '13', '23:15:00', '9619']
# 0 1 2 9 Correct!


# Great job. You've earned the flag: picoCTF{w4y_0ut_940df760}

# [*] Closed connection to 2018shell2.picoctf.com port 39410
# [Finished in 3.6s]