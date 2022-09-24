#1
x ="Global"
def my_fun():
	x="Local"
	print(x)
my_fun()
print(x)

#2
def my_fun1():
	print("I am in my fun")
	def my_gun():
		print("I am in my gun")
		def kanif():
			print("I am in Kanifnath")
			def kanif1():
				print("I am in Kanifnath1")
			kanif1()
		kanif()
	my_gun()
my_fun1()

#nested function only calls from outer function.we can write more than one nested functions

#3
def my_outer():
	x="Outer"
	def my_inner():
		nonlocal x
		x ="Inner"
		print(x)
	my_inner()
	print(x)
my_outer()

#nonlocal variable is only accesible upto outer function it is not be global and we can do nonlocal variable in inner function only