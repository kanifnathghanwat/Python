#keyword argument
def my_fun(name,age):
	print(f"Hello,my name is {name} and I am {age} years old")
print(my_fun(age=25,name="Kanifnath"))

#default argument
def my_fun(name,age=25):
	print(f"Hello,my name is {name} and I am {age} years old")
print(my_fun("Kanifnath"))

#require argument
'''def my_fun(name,age):
	print(f"Hello,my name is {name} and I am {age} years old")
print(my_fun("Kanifnath"))'''

#variable number of argument
def my_fun(name,*kwarg):
	print(name)
	for i in kwarg:
		print(i)
	print(type(kwarg))
print(my_fun("Kanifnath",10,20,30))
print(my_fun("Kanif",10,50,70,90,56))