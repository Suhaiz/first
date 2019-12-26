# x=int(input("enter your no\t"))
# lst=str(x)
# dig1=min(lst)
# dig2=max(lst)
# print(dig2)
# divisor=dig1+dig2
# # divisor="".join([dig1,dig2])
# div=int(divisor)
# print(div)
# if x%div==0:
#     print(x,"\tis a gapful no")
#
#


x=int(input())
lst=str(x)
dig_1=lst[0]
dig_2=lst[len(lst)-1]
divisor="".join([dig_1,dig_2])
if(x%int(divisor)==0):
    print("the no is a gapful no")
else:
    print("its not a gapful no")

