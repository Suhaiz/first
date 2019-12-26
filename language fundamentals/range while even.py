upperlimit=int(input("enter your upper limit\t\n"))
lowerlimit=int(input("enter your lower limit\t\n"))
i=lowerlimit
sum=0
while(i<=upperlimit and i>=lowerlimit):
    if(i%2==0):
        print(i)
        sum=sum+i
    i=i+1
    
print("your sum is",sum)