#1
def my_fun(**arg):
	print(arg)
	
my_fun(value=10,value1=20,value2=30,value3=40)
print("\n\n")

#2
def my_fun1(**arg):
	for key,value in arg.items():
		print(f"{key} : {value}")
	
my_fun1(value=10,value1=20,value2=30,value3=40)
print("\n\n")

#3
def my_fun2(*kwarg):
	for i in kwarg:
		print(i)
		print(type(kwarg))
		
my_fun2(10,20,30)
my_fun2(10,20)
print("\n\n")

#4
def my_fun3(*arg,**kwarg):
	print(arg)
	print(kwarg)
	print(type(arg))
	print(type(kwarg))

my_fun3(20,30,40,50,name="Hello",value=53)
my_fun3(10,20)