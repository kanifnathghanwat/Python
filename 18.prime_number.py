no=int(input("Enter a number to check prime or not: "))
#temp=0

for i in range(2,no):
	flag=False
	if no%i==0:
		flag=True
		break

if flag==False:
	print(f"{no} is Prime")
else:
	print(f"{no} is not Prime")