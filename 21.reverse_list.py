user=int(input("How number of list you want: "))
l=[]
n=[]
for i in range(user):
    num=int(input("Enter  number in list: "))
    l.append(num)
print(f"Your real number list is: {l}")
n=l.copy()
n.reverse()
print(f"Your revers number list is: {n}")