

# str=input()
#
# l=len(str)
#
# for i in range(len(str)):
#     for j in range((l/2),l):
#         if str[i]==str[j]:
#             if str[i+1]==str[(l/2)+1]:
#
#


# import re
# from re import fullmatch
#
# str=input()
# count=0
# if re.fullmatch(r"^(.+)\1+$",str):
#     print("not prime")
# else:
#     print("prime")




#
#
# str=input() or "abcabc"
#
# def pri_string(str):
#     for i in range(1,1+len(str)//2):
#         pattern=str[i:]
#         a=len(str)//i
#         if pattern*a==str:
#             return str+" is not prime"
#     return str+ " is prime"
#
# print(pri_string(str))
#

# print(lambda str:pattern=str[:i]*i for i in range(1,1+len(str)//2)
#

w=input()
print(w+" is not prime" if w[:len(w)//2]==w[len(w)//2:] else w + " is prime")