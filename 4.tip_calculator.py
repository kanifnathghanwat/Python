print("Tip Calculator")
amount=int(input("Enter your total bill amount: "))
tip=int(input("Enter Tip percent: "))
person=int(input("Total number of Person: "))
tip=(amount*tip)/100
tip=amount+tip
tip=tip/person
print(f"Each Person will pay: {round(tip,2)}")8