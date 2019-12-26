import re

f1=open("/home/suhaiz/PycharmProjects/luminarpython/test/emails",'r')
f2=open("valid_mails",'w')
lst=[]
count=0
for item in f1:
    lst=item.rstrip("\n")
    x='[a-z][a-z0-9]*@[a-z0-9]*.com'
    matcher=re.fullmatch(x,lst)
    if matcher!=None:
        f2.write(lst)
        f2.write("\n")
        count+=1

print("total no of valid mail id's are \t",count)
