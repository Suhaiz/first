no1=int(input("enter first no  "))
no2=int(input("enter second no  "))
no3=int(input("enter third no  "))

if(no1>no2):
    if(no1>no3):
        print("the first no you entered is the greatest")
        if(no2>no3):
            print(no1,">",no2,">",no3)
    else:
        print(no3,">",no1,">",no2)
elif(no2>no3):
    print(no2,"is max")
    if(no1>no3):
        print(no2,">",no1,">",no3)
    else:
        print(no2, ">", no3, ">", n1)
else:
    print(no3,"is the greatest")
    if (no1 > no2):
        print(no3, ">", no1, ">", no2)
    else:
        print(no3, ">", no2, ">", no1)

