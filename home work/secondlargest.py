#program to find the second largest no from the list using sa single forloop

lst=[14,4,3,6,8]

lst1=sorted(lst)
print(lst1)

for i in range (len(lst1)):
    print(lst1[i+1],"is the second largest item in the list")
    break