##lambda functions are anonymous functions which are nameless functions used to reduce the size of the codes
##boiler plate code:::to repeat a particular task
#
# def square(no):
#     return no**2
#
#
# ##the corresponding lambda function of this function is as shown below which will only have the argument and the function syntax
# #
# # f=lambda no:no**3
# # print(f(5))
# #
# # def cube(nu):
# #     return nu**3
# #
# # f1=lambda nu:nu**3
# # print(f1(3))
#
# #
# f2=lambda no1,no2,no3:no1+no2
# print(f2(4,5,6))
#
# f3=lambda word:len(word)
# print(f3("hello"))

#
# ls=[1,2,3,4,5]
#
# def sqr(lst):
#     for i in range(len(lst)):
#         print(lst[i]*lst[i],end=" ")
#
#
# sqr(ls)

print((lambda n,a:(n**2,n+2,a+10))(*input().split()))
