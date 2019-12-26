number=int(input("input any no\t\t"))
i=2
t=0
range=int(input("enter a range"))
z=0
while(i<=(number-1)):
    if(number%i==0):
        t=t+1
        break
    else:
        t=0
    i=i+1
if(t>0):
    print(number,"is not a prime no")
else:
    print(number,"is a prime no")

