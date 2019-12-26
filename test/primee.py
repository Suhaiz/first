upplim=int(input("enter the upper limit\t"))
lowlim=int(input("enter the lower limit\t"))
sum=0

while lowlim<upplim+1:
    i=2
    flag=True
    while i<upplim:
        if upplim%i==0:
            flag=False
            break
        i+=1
    if flag:
        sum=sum+upplim
        print("\n",upplim)
    upplim-=1

print("your sum of prime no's is\t",sum)
