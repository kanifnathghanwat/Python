age=int(input("Enter your age: "))
year=90-age
days=year*365
weeks=days/7
months=year*12
if(age>90):
	print("You are already expire...!")
elif(age==90):
	print("You are close to death...!")
else:
	print("You have {} Days, {} Weeks, {} Months, {} Years left...!".format(days, int(weeks), months, year))