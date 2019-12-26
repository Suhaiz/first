lst1=[1,2,3]
lst2=[4,5,6]
lst3=[]

for i in lst1:
    for j in lst2:
        l=(i,j)
        lst3.append()

print(lst3)

##################################################3

# lst3=[(i,j) for i in lst1 for j in lst2]
# print(lst3)

###############################################
#
# lst3=[(i+j) for i in lst1 for j in lst2]
# print(lst3)

#################################################
#
# lst3=[(i) for i in lst1 if i%2==0]
# print(lst3)