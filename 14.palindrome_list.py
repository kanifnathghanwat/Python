no=int(input("Enter how many character you want in list: "))
l=[]
a=''
for i in range(no):
	value=input("Enter list character: ")
	l.append(value)
print(f"Your list is: {l}")

for i in l:
	a=a+str(i)

if(a==a[ : : -1]):
	print("List is palindrome")
else:
	print("List is not palindrome")