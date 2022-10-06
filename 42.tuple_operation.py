t = 10,20,30,40,"Hello",3.14,[100,200]
print(t)

print(t[5])
print(t[-1])
print(t[-1][0])
# t[0]=50

t=(10)
print(type(t))

t=(10,)
print(type(t))

t=(10,20,"Hello","Bye",3.14)
print(t)
print(t[2:])
print(t[:3])
print(t[::-1])

t1=(2.63,"Welcome",80)
print(t1)
print(t + t1)

t=(10,20,30,40,50)
print(t)
print(t[4])
print(t[4:])
print(t[5:])
# print(t[5:] + 100)

# add element in tupple
print(t[5:] + (100,))
print(t + (100,))
print(t[3:])
print(t[:3])
print(t[:3] + (1000,2000,3000) + t[3:])

# delete element from tuple
t=(1,2,3,4,5,6,7,8,9,10)
t=t[:3] + t[6:]
print(t)

t=(10,20,30,40,50)
print(t)
l=list(t)
print(l)
l.remove(30)
print(l)
t=tuple(l)
print(t)

del(t)
# print(t)

# length
t=(10,20,30,40,50)
print(len(t))