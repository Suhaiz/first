# lst1=[[10,"abc",15000],[11,"cde",20000],[12,"asd",25000],[13,"efg",30000]]
# count=0
# sum=0
# for item in lst1:
#     if(item[2]>15000):
#         count=count+1
#         sum=sum+item[2]
#         print(item)
# print(count)
# print("total salary is",sum)

lst2=[[1,"abc",1991,4],[2,"def",1992,4.5],[3,"ghi",1991,5.0],[4,"fff",1991,5.0]]
highest=0
for item in lst2:
    if(item[3]>highest):
        highest=item[3]

print("the highest rating of a movie is",highest)

for item in lst2:
    if(highest==item[3]):
        print(item)


