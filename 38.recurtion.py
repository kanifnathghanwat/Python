def my_fact(num):
	if num==0:
		return 1
	else:
		return num * my_fact(num-1)

a=int(input("Enter number for find factorial: "))
fact=my_fact(a)
print(f"Factorial is {fact}")

