num=int(input("enter a no\t"))
vari=num
sum=0
while(vari>0):
    temp=vari%10
    sum=sum+(temp*temp*temp)
    vari=vari//10
if(sum==num):
    print(num," is an armstrong no")
else:
    print(num,"is not an armstrong no")