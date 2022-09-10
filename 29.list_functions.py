l=[10,20,30]
print(l)
print(type(l))

#1
l.append(50)
l.append("Hello")
print(l)

#2
p=l.copy()
print(p)

#3
l.clear()
print(l)

#4
print(p.count(20))

#5
p.extend([15,25])
print(p)

#6
print(p.index("Hello"))
print(p.index(20,1))
print(p.index(30,2,6))

#7
p.insert(2,"Kanifnath")
print(p)

#8
print(p.pop(1))
print(p)

#9
p.remove(10)
print(p)

#10
p.reverse()
print(p)
print(p[1])

#11) sort only apply on homogenious data
a=[1,5,3,2,7,8,9]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.sort(reverse=False)
print(a)

b=['c','d','a','b','e','g','f']
b.sort()
print(b)
b.sort(reverse=True)
print(b)
b.sort(reverse=False)
print(b)
