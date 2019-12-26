f1=open("/home/suhaiz/PycharmProjects/luminarpython/forimporting/textw3",'r')
f2=open("found13count",'w')
list1=[]
dict1={}
for letter in f1:
    list1=letter.rstrip("\n")
for letter in list1:
    if letter not in dict1:
        dict1[letter]=1
    else:
        dict1[letter]+=1
print(dict1)

for i,j in dict1.items():
    i=str(i)
    j=str(j)
    f2.write(i)
    f2.write("\t")
    f2.write(j)
    f2.write("\n")
