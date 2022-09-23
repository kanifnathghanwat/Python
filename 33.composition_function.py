def add(num):
	sum=num+10
	return sum
	
def sub(num):
	res=num-5
	return res
	
ans=sub(add(10))  #composition
print(ans)

#composition means OP of one function is IP to another function