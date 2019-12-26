lst=[1,2,11,3,9,6,7,5]


lst=sorted(lst)
print(lst)
lower=0
upper=len(lst)
mid=(upper+lower)//2
length=len(lst)

element=int(input("\nenter the element to be searched\t"))
flag=0

while(lower<=upper):
    if(element>lst[mid]):
        lower=mid+1

    elif(element<lst[mid]):
        upper=mid-1

    elif(element==lst[mid]):
        print("\nthe element is found at the position",mid,"of the list\t",lst)
        flag+=1
        break

    mid=(lower+upper)//2

if(flag==0):
    print("the element is not found")
