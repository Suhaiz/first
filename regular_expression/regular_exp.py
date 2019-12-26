###regular expressions are used to find matches

import re
count=0
matcher=re.finditer('ab','abaababa')
for match in matcher:
    print("match available at",match.start())
    print("group=",match.group())
    count+=1
print("count=",count)


# import re
# count=0
# x='[abc]'
# matcher=re.finditer(x,'a7ba@k9z')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())
#     count+=1


# import re
# count=0
# x='[^abc]'
# matcher=re.finditer(x,'ahfbehvberuf')
# for match in matcher:
#     print("match availble at",match.start())
#     print("group=",match.group())
#     count+=1



#
# import re
# count = 0
# x = '[a-z]'
# matcher = re.finditer(x, 'ahfbehvberuf')
# for match in matcher:
#     print("match availble at", match.start())
#     print("group=", match.group())
#     count += 1
#

# x='[A-Z]'
# X='[0-9]'





# import re
# count = 0
# x='[a-zA-Z0-9]'
# matcher = re.finditer(x, 'ahfbehvbe r123uf')
# for match in matcher:
#     print("match availble at", match.start())
#     print("group=", match.group())
#     count += 1
#
#Predefined characters
# x='[^a-zA-Z0-9]'
# x='\s' is used to find the space
# x='\d'  is used to find the digits
# x='\D' is used to find all the other characters except digits
# x='\w' is used to find all the alphanumerical
# x='\W' is used to find all the special characters

#
# import re
# count = 0
# x='\w'
# matcher = re.finditer(x, 'ahfbehvbe r123uf')
# for match in matcher:
#     print("match availble at", match.start())
#     print("group=", match.group())
#     count += 1
#
#  predefined character set
# '[abc]'
# '[^abc]'
# '[a-z]'
# '[A-Z]'
# '[0-9]'


##############################################QUANTIFIERS

# import re
# count = 0
# x='a+'
# matcher = re.finditer(x, 'abaabaaabbababbab')
# for match in matcher:
#     print("match availble at", match.start())
#     print("group=", match.group())
#     count += 1

# x='a+'
# x='a*'
# x='a?'
# x='a{m}'
# x='a{2,3}'
# x='^a'

# import re
# count = 0
# x='a*'
# matcher = re.finditer(x, 'abaabaaabbababbab')
# for match in matcher:
#     print("match availble at", match.start())
#     print("group=", match.group())
#     count += 1

# a illaatha positionsum kaanikkum a ulla positionsum kaanikkum


# import re
# count = 0
# x='a?'
# matcher = re.finditer(x, 'abaabaaabbababbab')
# for match in matcher:
#     print("match availble at", match.start())
#     print("group=", match.group())
#     count += 1
#
# individual a'sum count cheyyum a illaatha positionsum count cheyyum
#
#
# x='a{3}'

# 3 a aduppich vannal count cheyyum

#x='a{2,4}'
# min 2 a ullathum maximum 4 a ullathum edukkum

import re
count = 0
x='^a'
matcher = re.finditer(x, 'bab aaabbababbab')
for match in matcher:
    print("match availble at", match.start())
    print("group=", match.group())
    count += 1


# x='^a' ,   a vechaano start cheyyunnath ennu check cheyyum
# x='$a' , ending with a anno ennu check cheyyum


#########################################################################################  USING FULLMATCH


# import re
#
# x='[a-kA-K][369][a-zA-Z@$]*'
# a=input("enter your string")
# count=0
# matcher=re.fullmatch(x,a) #all positions or rules should be correct
# if matcher!=None:
#     print("valid")
# else:
#     print("invalid")
#

#####################################################################################validate vehicle no's

# import re
#
# # x = '[K][L][\d][\d][A-Z][A-Z][\d][\d][\d][\d]'
# x='KL\d{2}[A-Z]{2}\d{4}'
# a = input("enter your string")
# count = 0
# matcher = re.fullmatch(x, a)  # all positions or rules should be correct
# if matcher != None:
#     print("valid")
# else:
#     print("invalid")

#################################################################################phoneno

# import re
#
# x='[6-9]\d{9}'
# a = input("enter your string\t")
# count = 0
# matcher = re.fullmatch(x, a)  # all positions or rules should be correct
# if matcher != None:
#     print("valid")
# else:
#     print("invalid")

#########################################################################################

# import re
#
# f1=open("/home/suhaiz/PycharmProjects/luminarpython/regular_expression/phoneno",'r')
# f2=open("validphoneno",'w')
# lst=[]
#
# for no in f1:
#     lst=no.rstrip('\n')
#     print(lst)
#     x='[6-9]\d{9}'
#     matcher = re.fullmatch(x,lst)  # all positions or rules should be correct
#     if matcher != None:
#         print(lst," is valid")
#         f2.write(lst)
#         f2.write('\n')
#     else:
#         print(lst,"is invalid")
#
#

#######################################################################################email.com

# import re
#
# x='[a-z][a-z0-9]*@gmail.com'
# a = input("enter your string\t")
# count = 0
# matcher = re.fullmatch(x, a)  # all positions or rules should be correct
# if matcher != None:
#     print("valid")
# else:
#     print("invalid")
