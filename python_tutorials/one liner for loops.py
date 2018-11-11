a=[[1,2],[3,4],[5,6],[6,7]]

sum=sum(value for item in a for value in item if value%2==0 and value%3==0)

print('sum:',sum)
