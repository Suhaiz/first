# a=[4,3,2,5]
# b=len(a)
# max=a[0]
# for item in a:
#     if(item>max):
#         max=item
# print(max)

# a="aaaa"
# b=len(a)
# print(b)

# def matchword(words):
#     ctr=0
#
#     for item in words:
#         leng = len(item)-1
#         if(item[0]==item[leng]):
#             ctr+=1
#     return ctr
#
# print(matchword(["abc","cbc","ddd","zzz","ebekabkfbe"]))

# a=[1,2,3,4,5,6,7,8,9,0,0,9,8,7,6,5]
# uniq_items=[]
# dup_items=set()
#
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
#
# print(dup_items)
# print(uniq_items)



# def func(n,str):
#     txt=str.split(" ")
#     list1=[]
#     for item in txt:
#         if (len(item)>n):
#             list1.append(item)
#     print(list1)
#
#
# func(3,"the quick brown fox jumps over the lazy dog")


# list=[1,2,3,4,5,6]
#
# for i in range(0,len(list)-1):
#     if(i==0 or i==4 or i==5):
#         del list[i]
# print(list)

# array=[["*" for col in range(4)] for row in range(2)]
# print(array)

# a=[1,2,3,4,5,6,7,8,9]
# b=[item for item in a if item%2==0]
# print(b)

from random import shuffle as s
color=["red","blue","green","yellow"]
s(color)
print(color)







