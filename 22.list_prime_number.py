no=int(input("Enter How many numbers you want in list: "))
l=[]
l_prime=[]
l_non_prime=[]

for i in range(no):
	value=int(input("Enter number in list: "))
	l.append(value)
print(f"Your list is: {l}")

for j in l:
	flag=False
	for i in range(2,j):
		if j%i==0:
			flag=True
			break
		
	if flag==True:
		l_non_prime.append(j)
	else:
		l_prime.append(j)
		
print(f"Prime number list: {l_prime}")
print(f"Non prime number list: {l_non_prime}")