no=int(input("Enter a number: "))
rev=0
while range(no!=0):
	r=no%10
	rev=rev*10+r
	no=int(no/10)
print(f"Reverse number is: {rev}")