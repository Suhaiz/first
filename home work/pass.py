f1=open("/home/suhaiz/PycharmProjects/luminarpython/home work/students",'r')
f2=open("/home/suhaiz/PycharmProjects/luminarpython/home work/failed",'r')
f3=open("/home/suhaiz/PycharmProjects/luminarpython/home work/passed",'w')

list1=[]
list2=[]
set1=set()
set2=set()

for name in f1:
    print(name)
    list1=name.rstrip("\n").split(",")
for name in f2:
    list2=name.rstrip("\n").split(" ")

# print(list1)
# print(list2)
set1=set(list1)
set2=set(list2)
print(set1)
print(set2)
set3=set1-set2
print(set3)

for w in set3:
    f3.write(w)
    f3.write("\t")


