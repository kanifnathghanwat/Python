name1 = input('Enter King name: ')
name2 = input('Enter Queen name: ')
name = name1 + name2
name = name.upper()
L = name.count('L')
O = name.count('O')
V = name.count('V')
E = name.count('E')

T = name.count('T')
R = name.count('R')
U = name.count('U')
E = name.count('E')

a = (str(L+O+V+E) + str(T+R+U+E))
if(int(a) > 100):
     print("100% YES YOUR LOVE IS TRUE")
else:
    print("Percentage of u both LOVE: ",str(L+O+V+E) + str(T+R+U+E) + "%")