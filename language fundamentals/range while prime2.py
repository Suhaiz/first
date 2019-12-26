rang=int(input("enter a range\t"))
number=2
flag=0
i=2
while(number<=rang):
    while (i >= 2 and i < number):
        if (number % i == 0):
            flag = flag + 1
            break
        else:
            i = i + 1
            flag = 0
        if (flag == 0):
            print(number, "is a prime no")
            number = number + 1
    number = number + 1


