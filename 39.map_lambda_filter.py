# 1)
def my_square(num):
	return num * num

print("Simple function: ",my_square(11))

# 2)
# ret=lambda arg1,arg2,argn: expression
def add(num):
	return num+num
	
ret=lambda  num:num*num
print("Lambda: ",ret)

# 3)
#filter(function,iterable_object)

def my_fun(num):
	if(num>50):
		return num

result=tuple(filter(my_fun,[10,20,60,70,30]))
print("Filter: ",result)
print(type(result))

# 4)
l=[10,20,30,40,50,60,70]
l1 = list(filter(lambda num : (num > 50),l))
print("Lambda function: ",l1)

# 5)
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# 6)
def my_square1(num):
	return num*num

l=list(map(my_square1,[2,4,6,8]))
print("Map: ",l)
l1=list(map(lambda num:num*num,[2,4,6,8]))
print("Map: ",l1)