#string writing pattern
s="Hello's"             #single '
s1='Hello "hii"'       #single " "
s2='''Hello's "hii"'''   #double ' & " "
print(s)
print(s1)
print(s2)

#string functions
s="Hello my name is Kanifnath Adinath Ghanwat"
print(s.capitalize())   #only 1st letter capital
print(s.count('a'))
print(s.count('Ka'))
print(s.center(50))
print(s.center(50,"#"))
print(s.endswith('Ghanwat'))
print(s.find("Ka"))
print(s.index('i'))
print(s.index('is'))
print(s.islower())
print(s.isupper())
print(s.upper())
print(s.lower())
print(s.replace('Hello','Hii'))
print(s.expandtabs())
print(s.title())
print(s.zfill(50))
print(s.split())
print(type(s.split()))
s=s.split()
print(s[4])

s="Hellow Python \ welcome"
print(s)
s="Hellow Python\n welcome"
print(s)
s="Hellow Python\t welcome"
print(s)
s="Hellow all\'s Python welcome"
print(s)
s="Hellow Python\"s welcome"
print(s)