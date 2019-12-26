##single inheritance

# class base:
#     def m(self):
#         print(" inside the base class")
#
# class derived(base):
#     def m2(self):
#         print("inside derived class")
#
# ob=derived()
# ob.m2()
# ob.m()

#######################################method overiding

class base:
    def m(self,a):
        print(" inside the base class")

    def m3(self):
        print("inside base class")

class derived(base):
    def m(self):
        print("inside derived class")

ob=derived()
ob.m(1)


#################################  multi level inheritance

class A:
    def m(self):
        print("inside A")

class B(A):
    def m1(self):
        print("inside B")

class C(B):
    def m2(self):
        print("inside C")

c=C()
c.m()
c.m1()
c.m2()

