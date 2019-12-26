lst=[1,2,11,3,9,6,7,5]


lst=sorted(lst)
print(lst)
lower=0
upper=len(lst)
mid=(upper+lower)//2
length=len(lst)

element=int(input("\nenter the element to be searched\t"))

for i in range(0,length-1):
    if(element>lst[mid]):
        lower=mid+1

    elif(element<lst[mid]):
        upper=mid-1

    elif(element==lst[mid]):
        print("\nthe element is found at the position",mid,"of the list\t",lst)
        break

    else:
        print("\nthe searched element",element,"is not in the list\t",lst)
        break
    mid=(lower+upper)//2
