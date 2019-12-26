range=int(input("enter a range\t"))
number=2
flag=0
i=2
while(number<=range):
    while(i<=number):
        if(number%i==0):
            flag=flag+1
            number=number+1
            break
        else:
            flag=0
            i+=1
    if(flag==0):
        print(number,"is a prime no")
    else:
        print(number,"is not a prime no")
