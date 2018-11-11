L=[1,2,3,4,5,6,7,8,9,10]

T=1,2,3,45,6,7,8,9,10

print(hex(id(L)))
L.append(11)
print(hex(id(L)))

T.append(11)

