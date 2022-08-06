import random
digit=int(input("Enter how many digit OTP you want: "))
l=['0','1','2','3','4','5','6','7','8','9']
otp=[]
a=''
for i in range(digit):
	value=(random.choice(l))
	otp.append(value)

for i in otp:
	a=a+str(i)
print(f"Your OTP is: {a}")
