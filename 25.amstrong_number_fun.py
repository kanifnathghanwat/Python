def amstrong_num(num):
	sum=0
	order=len(str(num))
	while num>0:
		digit=num%10
		sum=sum+ digit ** order
		num=num // 10
	if temp==sum:
		return True
	else:
		return False
temp=no=int(input("Enter a number: "))
if amstrong_num(no)==True:
	print("{} is amstrong number".format(no))
else:
	print("{} is not amstrong number".format(no))