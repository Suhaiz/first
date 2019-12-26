name=input("enter students name  ")
a=int(input("enter the marks for the first subject  "))
b=int(input("enter the marks for the second subject  "))
c=int(input("enter the marks for the third subject  "))
total=a+b+c
if(total>=140):
    print("the grade is A+")
elif(total<140 and total>=130):
    print("the grade is A")
elif(total<130 and total>=120):
    print("the grade is B+")
elif(total<120 and total>=110):
    print("the grade is B")
elif(total<110) & (total>=100):
    print("the grade is C+")
else:
    print("Fail")