f1=open("/home/suhaiz/PycharmProjects/luminarpython/fileinputout/totalwords",'r')
f2=open("countedwords",'w')
lst1=[]
dict1={}
for item in f1:
    lst1=(item.rstrip("\n").split(","))
    print(lst1)
    for word in lst1:
        if word not in dict1:
            dict1[word]=1
        else:
            dict1[word]+=1
print(dict1)

for i,j in dict1.items():
    i=str(i)
    j=str(j)
    f2.write(i)
    f2.write("\t")
    f2.write(j)
    f2.write("\n")

