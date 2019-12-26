#refer=open('filepath','mode')
#3 types
#read-------r
#write------w
#read and writ-----r+
#write and read-----w+
#append----------a

# refer=open("/home/suhaiz/PycharmProjects/luminarpython/forimporting/txt",'r')
# lst=[]
# for word in refer:
#     # lst.append(word)
#     lst.append(word.rstrip("\n"))
# print(lst)

# refer1=open("/home/suhaiz/PycharmProjects/luminarpython/forimporting/even",'r')
# lst1=[]
# lst2=[]
# for no in refer1:
#     lst1.append(no.rstrip("\n"))
# print(lst1)
#
# for i in lst1:
#     num=int(i)
#     if num%2==0:
#         print(num)

# for i in lst1:
#     if(i%2==0):
#         lst2.append(i)
#
# print(lst2)



###############################################################################################

f=open("/home/suhaiz/PycharmProjects/luminarpython/forimporting/txt2")
print(f.mode)