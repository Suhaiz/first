f1=open("/home/suhaiz/PycharmProjects/luminarpython/fileinputout/place_temp",'r')
f2=open("final_temp",'w')
dict={}
lst=[]

i=0

for item in f1:
    lst=item.rstrip("\n").split(",")
    print(lst)
    if lst[i] not in dict:
        dict[lst[i]]=lst[i+1]
        continue
    elif lst[i+1]>dict[lst[i]]:
        dict[lst[i]]=lst[i+1]
    else:
        continue
print(dict)


for i,j in dict.items():
    i=str(i)
    j=str(j)
    f2.write(i)
    f2.write("\t")
    f2.write(j)
    f2.write("\n")



