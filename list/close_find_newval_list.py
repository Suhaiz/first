lst1=[2,3,4,5,6]

b=[360,240,180,144,120]            # THE RESULT SHOULD BE LIKE THIS

lst2=[]
print(lst1)

# val = lst1.pop(0)
# lst2[i] = lst1[0] * lst1[1]

# for z in range(0,3):
#     for i in range(0,3):
#         for j in range(0,3):
#             if (z != i and z != j):
#                 if(i!=j):
#                     if(i<j):
#                         lst2.append(lst1[i] *lst1[j])
#
# print(lst2)
#
#
###################################################################3
# i=0
# lst3=[]
# while(i<len(lst1)):
#     val=lst1.pop(0)
#     lst2.append(lst1[0]*lst1[1])
#     i+=1
#     lst1.append(val)
# print(lst2)
######################################################################

i=0
lst3=[]
while(i<len(lst1)):
    val=lst1.pop(0)
    lst2.append(lst1[0]*lst1[1]*lst1[2]*lst1[3])
    i+=1
    lst1.append(val)
print(lst2)


