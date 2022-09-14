no=int(input("How many elements you want in list: "))
l=[]
for i in range(no):
	value=int(input("Enter list element: "))
	l.append(value)
print(l)
no_remove=int(input("Enter element to remove: "))

i=0
while i<no:
	if no_remove==l[i]:
		l.remove(l[i])
		i=i-1
		no=no-1
	i=i+1
print(l)




#for i in l:
#	if no_remove==i:
#		l.remove(i)
#print(l)