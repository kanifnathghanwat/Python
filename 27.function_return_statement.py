def my_fun():
	c=10+20
	return c
	d=20-10
	return d  #unreachable statement
print(my_fun())

#tuple
def my_fun1():
	c=10+20
	d=10+5
	return c,d
print(my_fun1())

#list
def my_fun2():
	c=10+20
	d=10+5
	return [c,d]
print(my_fun2())
print(type(my_fun2()))

#set
def my_fun3():
	c=10+20
	d=10+5
	return {c,d}
print(my_fun3())
print(type(my_fun3()))

#dictionary
def my_fun4():
	c=10+20
	d=10+5
	return {c:d}
print(my_fun4())
print(type(my_fun4()))


#retun statement always returns one object so here c,d are in one object i.e. by default in tuple.If we give [c,d] then it gives OP in list, when give {c,d} then OP in set, when give {c:d} then OP in dictionary. In the form {key:value}...        In one function we can return value only once but we can call the function more than once.