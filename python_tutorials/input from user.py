import sys
print('input from command line',end='')
print(sys.argv)

name=input('Name    : ')
print(name)

marks=[]
for i in range(3):
    marks.append(int(input('Enter marks for subject-'+str(i)+' : ')))

print(marks)

