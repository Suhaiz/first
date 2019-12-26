lst=[]
a=int(input("\nenter how many elements you want to store in the list\t"))
for i in range(0,a):
    element=int(input("\nenter your element\t"))
    lst.append(element)

print("\nyour original list is        \t",lst)


lsteven=[]
lstodd=[]
for i in range(0,a):
    if(lst[i]%2==0):
        lsteven.append(lst[i])
    else:
        lstodd.append(lst[i])

print("\nyour list of even numbers is\t",lsteven)
print("\nyour lis of odd numbers is  \t",lstodd)