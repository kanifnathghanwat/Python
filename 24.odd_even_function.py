def odd_even(num):
	if num%2==0:
		return True
	else:
		return False
no=int(input("Enter a number: "))
if odd_even(no)==True:
	print("{} is even".format(no))
else:
	print("{} is odd".format(no))
