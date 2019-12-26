# many forms...........same name different functionalities
#
# 1.method overloading

# implements in the same class
#     so there will be two methods with the same name inside a class but different parameters

# doesnt support directly in python

# 2.memaththod overiding

# inheritance is mandatory

# class parent:
#     def phone(self):
#         print("i have nokia 1166")
#
# class child:
#     pass
#
# o=child()
# o.phone()


# example for method overiding
class parent:
    def phone(self):
        print("i have nokia 1166")

class child:
    def phone(self):
        print("i have samsung")

o=child()
o.phone()
# 3.operator overloading