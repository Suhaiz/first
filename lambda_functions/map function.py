# lst=[1,2,3,4,5]
#
# def square(num):
#     return num*num
#
# a=list(map(square,lst))
#
# print(a)
################################################################sum

# lst2=[1,2,3,4,5]
#
# def doub(a):
#     return a+a
#
# b=list(map(doub,lst2))
#
# print(b)

##or you can avoid the normal function by bringing the lambda function

lst3=[1,2,3,4]

# z=list(map(lambda no:no+no,lst3))
# print(z)

#################################to get even numbers

# def even(no):
#     return no%2==0
#
# m=list(filter(even,lst3))
#
# print(m)

################################now using lambda in filter

# n=list(filter(lambda no:no%2==0,lst3))
# print(n)

################################veryimportanttttttttttttttttttttttttt

v=list(map(lambda no:no**2,filter(lambda no:no%2==0,lst3)))
print(v)

##################################################################
# v=list(filter(lambda no:no%2==0,(filter(lambda no:no**2,lst3))))
# print(v)