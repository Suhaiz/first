f1=open("words",'r')
f2=open("countwords",'w')
list1=[]
set1=set()
dict={}
for i in f1:
    list1=i.rstrip("\n").split(",")
    for i in range(len(list1)):
        if list1[i] not in dict:
            dict[list1[i]]=1
            continue
        else:
            dict[list1[i]]+=1
print(dict)

for i,j in dict.items():
    f2.write(i+"-")
    j=str(j)
    f2.write(j+"\n")
