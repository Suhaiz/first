# lst=[]
# for i in range(1,11):
#     lst.append(i*i)
# print(lst[:5])
# print(lst[3:])


# import itertools
# print(list(itertools.permutations([1,2,3])))

# list1=[1,2,3,4]
# list2=[1,2]
# list3=list(set(list1)-set(list2))
# print(list3)

# for numindex,numval in enumerate(list1):
#     print(numindex,numval)

# s=['a','c','d']
# print(s)
# str1=''.join(s)
# print(str1)

# colors1='red','blue','green'
# colors2='red','green'
# print(set(colors1) and set(colors2))
#
# color3="".join(colors1)
# print(color3)
#
# numbers=[11,22,33]
# new_numbers="".join(map(str,numbers))
# print(new_numbers)


################################################################################# beauty#######finding pair from list

def func(xs,k):
    flag=False
    for i in xs:
        if(flag):
            break
        for j in range(0,len(xs)):
            if(i!=xs[j]):
                if((i+xs[j])==k):
                    print("the values",i,xs[j],"add upto",k)
                    flag=True
                    break
                else:
                    flag=False

    if(flag==False):
        print("no values in the list add upto",k)


func([1,2,3,4,5,6,7,8,9,10],12)

###########################################################################################3

# from os.path import join
#
# a=['a','b','c','d']
# # print(a.index('b'))
# m="".join(a)
# print(m)

#########################################################################################

# list1=[1,5,2,4,3,8,6,7]
# list2=sorted(list1)
# upper=len(list2)-1
# lower=0
# k=int(input("enter any value\t"))
# list3=[1,2,3,4,5,6,7,8]
# for i in range(0,len(list2)-1):
#     if(k==list2[upper]+list2[lower]):
#         print("your value is equal to the sum of",list2[upper],"and",list2[lower])
#         break
#     elif(k<list2[upper]+list2[lower]):
#         upper=upper-1
#     elif(k>list2[upper]+list2[lower]):
#         lower=lower+1


