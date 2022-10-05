l = [2,3,4,5,6,7,8]

#def my_cube(x):
#	return x*x*x

#p=list(map(my_cube,l))
# p [8,27,64,125,216,343]

#def my_filter(x):
#	if x>100:
#		return x

#n=list(filter(my_filter,p))

n=list(filter(lambda y : y if y>100 else None,map(lambda x : x*x*x,l)))
print("Final list: ",n)