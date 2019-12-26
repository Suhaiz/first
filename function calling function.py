def add(a,b):
    sum=a+b
    return sum

c=int(input("enter any no\t"))
d=int(input("enter any no\t"))
result=add(c,d)

def oddeven(result):
    if(result%2==0):
        print(result,"is even")
    else:
        print(result,"is odd")



oddeven(result)


