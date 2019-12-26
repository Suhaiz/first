class parent1:
    def m1(self):
        print("inside parent1\n")

class parent2(parent1):
    def m2(self):
        print("inside parent2\n")

class child(parent2):
    def m3(self):
        print("inside child\n")

c=child()
c2=parent2()
c2.m2()
c.m1()
c.m2()
c.m3()























# java doesn have multiple inheritance instead it has interface
#but python supports multiple inheritance