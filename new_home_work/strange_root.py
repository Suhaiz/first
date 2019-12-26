# no=int(input("enter any no\t"))
# square=no**2
# str_sqr=str(square)
# print(square)
# root=no**0.5
# sroot=str(root)
# print(sroot)
#
# z="{:.3f}".format(root)
# print(z)
#
# if set(str_sqr)&set(str(z)):
#     print(no," has a strange root")
# else:
#     print("no strange root")
#

(lambda no,sq,root:print( no,"has a strange root coz common in",sq,"And",root) if set(str(sq))&set(str(root)) else print(no,"doesnt have a strange root"))(*(lambda n:(n,n**2,"{:.3f}".format(n**0.5)))(int(input("enter your no\t"))))


#######################################################  wrong
# print(set(str_sqr)&set(sroot))
# real_root=sroot.replace(".","")
# print(real_root)
# flag=0
# for i in range(len(str_sqr)):
#     if flag==1:
#         break
#     for j in range(len(real_root)):
#         if str_sqr[i]==real_root[j]:
#             print(no," has a strange root")
#             flag=1
#             break
#
# if flag==0:
#     print("the '{}' doesnt have a strange root".format(no))
#



# a=set("32.16351273657")
# b=set("7")
# print(a&b)



# strange=(lambda n:(n**2,n**0.5))(int(input())


# a=1
# b,a=a+1,a+2
# print(a,b)

# tup=(1,2,3,4)
# a,b,c,d=tup
# print(a,b,c,d,a)