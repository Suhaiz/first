# lis=[]
# print(type(lis))
# lst1=list()
# print(type(lst1))

# lst=[10,"10",10.2,True]
# print(lst)
lst1=[10,2,3,4]
# print(lst[1])

# a=len(lst1)
# for i in range(0,a):
#     if(lst1[i]%2==0):
#         print(lst1[i])


# for item in lst1:
#     print(item)

# sum=0
# for i in lst1:
#     sum=sum+i
# print("the sum is\t",sum)

# square=0
# for i in lst1:
#     square=i*i
#     print(square)



num=int(input("enter any number to check whether it is in the list\t"))
for item in lst1:
    if(num==item):
        flag=True
        break
    else:
        flag=False
        continue

if(flag):
    print(num, "is in the list\t", lst1)
else:
    print(num, "is not in the list\t", lst1)
