
lst=[7,2,3,4,5]
lst1=sorted(lst)
print(lst1)
upper=len(lst1)


for i in range(0,upper):
    if lst1[i]!=lst1[upper]-1:
        min=lst1[upper]-1
        upper=upper-1

    print(min)


