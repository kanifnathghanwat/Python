def list():
	no=int(input("How many number you want in list: "))
	list=[]
	for i in range(no):
		value=int(input("Enter list element: "))
		list.append(value)
	no1=int(input("Enter 1 for Ascending order list or 2 for Descending order list: "))
	return list,no1
	
a=list()
a1=a[0]
a2=a[1]

def sort(list,num):
	if num==1:
		list.sort(reverse=False)
		print(f"Ascending order list: {list}")
	if num==2:
		list.sort(reverse=True)
		print(f"Descending order list: {list}")
	
sort(a1,a2)

#ascending function
#def ascending(list,no1):
#	list.sort(reverse=True)
#	print(list)

#descending function
#def descending(list,no1):
#	list.sort(reverser=False)
#	print(list)


#if no1==1:
#	ascending(list,1)
#else:
#	decending(list,2)