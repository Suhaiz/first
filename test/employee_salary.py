class staff:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __str__(self):
        return self.name


f1=open("/home/suhaiz/PycharmProjects/luminarpython/test/employee_details",'r')
lst=[]
employees=[]

for line in f1:
    lst=line.rstrip("\n").split(",")
    print(lst)
    name=lst[0]
    age=lst[1]
    salary=lst[2]
    employees.append(staff(name,age,salary))

highsalary=list(filter(lambda o:int(o.salary)>15000,employees))

for ob in highsalary:
    print(ob)















highsalary=[]

for line in f1:
    lst=line.rstrip("\n").split(",")
    print(lst)
    # employees.append(staff(lst[0],lst[1],lst[2]))
    highsalary=list(filter(lambda o:int(o)>15000,lst[2]))

for ob in highsalary:
    print(ob)