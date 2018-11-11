# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)


temp=a*a if [] else b+b
print(temp)

temp=a*a if {} else b+b
print(temp)


p=[1,2,3,4,5,6]

print( "xyz" if len(p)==1 and True else "abc")


print('-------------------------------------------')

# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item (indexing is being used)
print(('a', 'b')[a < b])

# Use Dictionary for selecting an item
print({True: a, False: b}[a < b])

# lamda is more efficient than above two methods
# because in lambda  we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b*b, lambda: a*a)[a < b]())


