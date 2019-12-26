## the use of constructor is to initialise instance variables

# class student:
#     clgname="luminar"
#
#     def __init__(self,stname,id):
#         self.st_name=stname
#         self.id=id
#
#     def printval(self):
#         print("name=",self.st_name,end="\t")
#         print("id=",self.id)
#
# st=student("ajay",4005)
# st2=student("akshay",7000)
# st.printval()
# st2.printval()


# class book:
#     def __init__(self,pages):
#         self.pages=pages
#
# b1=book(100)
# b2=book(200)
# print(b1)
# doesnt work

# class book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __str__(self):
#         return str(self.pages)                         ##bcoz __str__ can only return string values   #alos define --str-- whenever you are printing objects
#
# b1=book(100)
# b2=book(200)
# print(b1)



##############operator overloading since + operator can only have 2 functions        string concat and integer addition
# but if we want to add two objects we need to invoke magic methods

# class book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __add__(self,other):
#         return book(self.pages+other.pages)
#
#     def __str__(self):
#         return str(self.pages)
#
# b1=book(100)
# b2=book(200)
# b3=book(400)
#
# print(b1+b2+b3)                          #########no matter how many objects are here in __add__ we need only only 2 arguements
#



class book:
    def __init__(self,pages):
        self.pages=pages

    def __sub__(self,other):
        return book(self.pages-other.pages)

    def __truediv__(self, other):
        return book(self.pages/other.pages)

    def __mul__(self,other):
        return book(self.pags*other.pages)

    def __str__(self):
        return str(self.pages)

b1=book(100)
b2=book(200)
b3=book(400)

print(b1-b2-b3)
print(b1/b2/b3)