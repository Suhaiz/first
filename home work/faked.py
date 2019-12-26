import operator

f1=open("/home/suhaiz/PycharmProjects/luminarpython/fileinputout/fakefriends.csv",'r')
lst=[]
dict={}
for age in f1:
    lst=age.rstrip("\n").split(",")
    print(lst)
    if lst[2] not in dict:
        dict[lst[2]]=1
    else:
        dict[lst[2]]+=1
print(dict)


# l=sorted(dict.values())
# print(l)
# for i,j in dict.items():
#     if dict[i]==l[-1]:
#         print(i,"-",j)

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
print(sorted_dict)
print(sorted_dict[-1])