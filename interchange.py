x=[1,2,3,4]
y=(len(x))
temp=x[0]
x[0]=x[y-1]
x[y-1]=temp
print(x)
