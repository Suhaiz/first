f1=open("/home/suhaiz/PycharmProjects/luminarpython/fileinputout/students_name",'r')
f2=open("/home/suhaiz/PycharmProjects/luminarpython/fileinputout/fail",'r')
f3=open("passed_students",'w')

set1=set()
set2=set()
for i in f1:
    set1.add(i.rstrip('\n'))
for w in f2:
    set2.add(w.rstrip('\n'))
set3=set1-set2
print(set3)

for i in set3:
    f3.write(i+"\n")
