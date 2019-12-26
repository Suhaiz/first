############static variable or classs variable.....accesed using classname....and instance variable which are self.

import datetime

class bank:
    bname="sbi"                                   #memory efficient usage is the function of a static variable
    def createaccount(self,acno,bal):
        self.accountno=acno
        self.balance=bal

    def deposit(self,amnt):
        self.balance+=amnt
        print("your new account balance is",self.balance,"since your",bank.bname," account has been credited with",amnt,"on",datetime.datetime.now())

    def withdraw(self, amt):
        if(amt>self.balance):
            print("insufficient balance")
        else:
            self.balance -= amt
            print("your new account balance is", self.balance, "since it has been debited with", amt, "on",datetime.datetime.now())

    def balance_enq(self):
        print("your account balance is",self.balance)


ob1=bank()
ob1.createaccount(1,10000)
ob1.deposit(5000)
ob1.withdraw(3000)
ob1.balance_enq()


ob2=bank()
ob2.createaccount(2,5000)
ob2.deposit(1000)

#######################################different types of methods

# 1. instance method
# 2. modify static variable is the function of class methods ..........using cls
#
# 3. static methods which do not have self.any



class student:

    schoolname="luminartechnolab"              # static or class variable
    def setval(self,id,name):
        self.id=id                                ###########self.id is the instance variable
        self.name=name

    def printval(self):
        print(self.id,"==",self.name,"==",student.schoolname)

    @classmethod                                  #decorator says the def below is the classmethod or staticmethod
    def setschool(cls,name):                      #instead of self we have self.....used to access static var and modify
        cls.schoolname=name

    @staticmethod
    def greetings():                               ##seperate futility function.......  invoked using class name
        print("welcome")


s=student()
s.setval(100,"noname")
s.printval()
s.setschool("luminar technolab sol")
s.printval()
student.greetings()

