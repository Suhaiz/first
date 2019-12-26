# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end="\t")
#     print()

# for i in range(1,4):
#     for j in range(1,i+1):
#         print(i,end="\t")
#     print()


# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end="\t")
#     print()
#

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="\t")
#     print()

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end="\t")
#     print()

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end="\t")
#     print()



def func_prime():
    ulimit=int(input("enter upper limit\t"))
    llimit=int(input("enter lower limit\t"))
    temp=ulimit
    while(temp>=llimit and temp<=ulimit):
        flag=True
        i=2
        while(i<temp):
            if((temp%i)!=0):
                i=i+1
                flag=True
            else:
                flag=False
                print(temp,"is not a prime no\t")
                break

        if(flag):
            print(temp,"is a prime no\t")
        temp=temp-1


func_prime()