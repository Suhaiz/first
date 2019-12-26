class person:
    def set(self,na,ag):
        self.name=na
        self.age=ag
    def disp(self):
        print("your name is",self.name)
        print("your age is",self.age)

ob1=person()
ob2=person()

ob1.set("ali",22)
ob1.disp()

print(ob1.age)


lst=[]
lst.append(ob1)
lst