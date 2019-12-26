lst=[0,1,2,3,4]
lst2=[]

result=0
for i in range(0,len(lst)):
    result+=lst[i]
    lst2.append(result)
print(lst2)

