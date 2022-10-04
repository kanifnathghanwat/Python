t=(10,20,30,40,50)
print(t)
print(type(t))

t=(10,20,30,40,50) #tuple packing

a,b,c,d,e=t    #tuple unpacking
print(a,b)

#errors
#t[2]=55
#t=(10,20,[5,"Hello",3.15],50)
#print(t)
#t[3]=55

l=["Hello",5,6,7,3.14]
t=(10,20,l,30,40)
print(t)
l[3]="Kanifnath"
print(t)

print(dir(t))