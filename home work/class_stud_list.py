class students:
    def roll(self,roll):
        self.rollno=roll
        print(self.rollno)

    def name(self,nam):
        self.name=nam
        print(self.name)

    def marks(self,mark):
        self.marks=mark
        print(self.marks)

    def disp(self,a,b,c):
        self.name=a
        self.roll=b
        self.marks=c
        print(self.name,self.roll,self.marks)

    def __str__(self):
        return self.name


ob1=students()
ob2=students()
ob3=students()


# ob1.disp("vijay",5,101)

f=open("/home/suhaiz/PycharmProjects/luminarpython/home work/stud_list",'r')

for word in f:
    lst=word.rstrip("\n").split(" ")
    print(lst)
    ob1.roll(lst[0])
    ob1.name(lst[1])
    ob1.marks(lst[2])
    if ob1.marks(lst[2])>100:
        print