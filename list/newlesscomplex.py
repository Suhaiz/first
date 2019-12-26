lst=[1,2,3,4,5,6,7,8]


lst=sorted(lst)
print(lst)
lower=0
upper=len(lst)
mid=(upper+lower)//2
length=len(lst)

element=int(input("\nenter the element whose sum pair should be found\t"))
flag=0

for i in range(0,len(lst)-1):
    for j in range(0,len(lst)-2):

        if(lst[i]+lst[j+1]==element):
            print("the pair found")
            flag+=1
            break

        else:
            flag=0
            continue


if(flag==0):
    print("the element is not found")