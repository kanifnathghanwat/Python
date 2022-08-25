no=int(input("How many number want in list: "))
l=[]
l1=[]
l2=[]

for i in range(no):
	value=int(input("Enter number in list: "))
	l.append(value)
print(f"Your list is: {l}")

for i in range(no):
	if l[i]%2==0:
		l1.append(l[i])
	else:
		l2.append(l[i])
print(f"Even number list: {l1}")
print(f"Odd number list: {l2}")
