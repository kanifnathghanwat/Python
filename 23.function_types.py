#function types based on input and output

# i)no IP no OP
def city():
	print("Ahmednagar")
city()

# ii)IP but no OP
def name(name1,name2):
	print(name1+name2)
name("NACSC"," Ahmednagar")

# iii)no IP but OP
num1=10
num2=20
def addition():
	return num1+num2
add=addition()
print("Addition: ",add)

# iv)IP and also OP
def addition(no1,no2):
	return no1+no2
print("Addition: ",addition(40,60))
	