##whenever there is an abnormal condition

# no1=int(input("enter any no"))
# no2=int(input("enter second no"))
# try:
#     res=no1/no2
#     print("res=",res)
# except:
#     print("exception occured")
#
# print("i have one database connection")
#

#################################################
#
# no1=int(input("enter any no"))
# no2=int(input("enter second no"))
# try:
#     res=no1/no2
#     print("res=",res)
# except:
#     no2=int(input("enter second no again"))
#     res=no1/no2
#     print("the result is",res)
#
# print("i have one database connection")

####################################################3

# no1=int(input("enter any no"))
# no2=int(input("enter second no"))
# try:
#     res=no1/no2
#     print("res=",res)
# except:
#     no2=int(input("enter second no again"))
#     try:
#         res=no1/no2
#         print("the result is",res)
#     except:
#         print("error occured")
#
# print("i have one database connection")

###################################################3

# no1=int(input("enter any no"))
# no2=int(input("enter second no"))
# lst=[1,2,3]
# try:
#     res=no1/no2
#     print("res=",res)
#     print(lst[5])
# except Exception as e:
#     print(e.args)
#
# print("i have one database connection")

#####################################################

no1=int(input("enter any no"))
no2=int(input("enter second no"))
lst=[1,2,3]
try:
    res=no1/no2
    print("res=",res)

except Exception as e:
    print(e.args)

try:
    print(lst[5])
except Exception as e:
    print(e.args)
finally:
    print("i have one database connection")
