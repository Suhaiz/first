class student:
    def roll(self,no):
        self.rollno=no
    def name(self,na):
        self.name=na
    def dis(self):
        print("the roll no is \t",self.rollno)
        print("the name is \t",self.name)
    def __str__(self):
        return self.name

ob1=student()
ob1.roll(23)
ob1.name("faiz")

ob2=student()
ob2.name("geeth")
ob2.roll(29)

ob2.dis()
ob1.dis()

lst=[]
lst.append(ob1)
lst.append(ob2)

for ob1 in lst:
    if ob1.rollno>=23:
        print(ob1)