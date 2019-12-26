lst1=[-5,-2,-7,99,100,105,103]
lst=sorted(lst1)

for j in range(0,len(lst)):
    if lst[j]<0:
        continue
    elif(lst[j+1]-lst[j])>1:
        print("the least positive integer is",lst[j]+1)
        break
