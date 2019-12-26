range=int(input("enter any range\t"))
maybeprime=2
flag=9
while(maybeprime<=range):
    num=2
    while(num<maybeprime):
        if(maybeprime%num==0):
            flag=False
            break
        else:
            flag=True
        num+=1
    if(flag):
        print(maybeprime, "is a prime no")
    maybeprime+=1