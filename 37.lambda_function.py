def my_square(x):
	return x*x

print("Simple function: ",my_square(10))

num=lambda x : x*x
print("Lambda function: ",num(15))

l = [42,36,20,46,47,69]
my_list = list(filter(lambda x:(x%2==0),l))
print("Even list: ",my_list)

import dis
print(dis.dis(my_square))
print(dis.dis(num))