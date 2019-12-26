import operator

f1=open("/home/suhaiz/PycharmProjects/luminarpython/fileinputout/fakefriends.csv",'r')
f2=open("age_count",'w')
lst=[]
dict={}
for i in f1:
    lst=i.rstrip("\n").split(",")
    print(lst)
    if lst[2] not in dict:
        dict[lst[2]]=1
    else:
        dict[lst[2]]+=1
print(dict)

for i,j in dict.items():
    f2.write(i)
    f2.write(" ")
    j=str(j)
    f2.write(j)
    f2.write("\n")

# sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
# print(sorted_dict)
# print(sorted_dict[-1])


l=sorted(dict.values())
for i,j in dict.items():
    if(l[-1]==j):
        print(i,j)


# for k,v in sorted(dict.items()):
#     print(k+"\t"+ str(v))
