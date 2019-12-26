# lst=["a","b","z"]
# f=open("text.txt",'w')
# for item in lst:
#     f.write(item+'\n')

ff=open("/home/suhaiz/PycharmProjects/luminarpython/forimporting/txt2",'r')
lst=[]
for word in ff:
    lst.append(word.rstrip("\n"))
fff=open("newtxt",'w')
for item in lst:
    fff.write(item+'\n')

#############################################################################################

ff=open("/home/suhaiz/PycharmProjects/luminarpython/forimporting/txt2",'r')
# lst=[]
# for word in ff:
#     lst.append(word.rstrip("\n"))
fff=open("newtxt2",'w')
for item in ff:
    fff.write(item)