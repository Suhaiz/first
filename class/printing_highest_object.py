class students:

    def __init__(self, id, name, total):
        self.id = id
        self.name = name
        self.total = total

    def __str__(self):
        return self.name


f1=open("/home/suhaiz/PycharmProjects/luminarpython/class/students",'r')
f2=open("writingobj",'w')

lst=[]
studentlist=[]

for line in f1:
    lst=line.rstrip("\n").split(",")
    print(lst)
    id=lst[0]
    name=lst[1]
    total=lst[2]
    studentlist.append(students(id,name,total))


mlist=list(filter(lambda o:int(o.total)>150,studentlist))

for ob in mlist:
    print(ob)

# for o in studentlist:
#     print((o.name).upper)

# upplist=list(map(lambda o:(o.name).upper,studentlist))
# for st in upplist:
#     print(st)