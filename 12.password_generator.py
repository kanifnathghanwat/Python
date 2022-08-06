import random

alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digit_list = ['0','1','2','3','4','5','6','7','8','9']
sybmol_list =['!','@','#','$','%','&','*']
password = []
passwrd = ''

alpha_count = int(input("Enter how many alphabates you want in your password ="))
digit_count = int(input("Enter how many digit you want in your password ="))
sybmol_count = int(input("Enter how many symbol you want in your password ="))

for i in range(alpha_count):
    value = random.choice(alpha_list)
    password.append(value)

for i in range(digit_count):
    value = random.choice(digit_list)
    password.append(value)

for i in range(sybmol_count):
    value = random.choice(sybmol_list)
    password.append(value)

random.shuffle(password)

for i in password:
    passwrd = passwrd+str(i)

print(f"Your password is: {passwrd}")
