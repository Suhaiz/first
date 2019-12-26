dict={101:"ab","z":"ac",103:"ad"}
# print(dict[101])
dict[101]="ABHI"
print(dict)

for item in dict.keys():
    print(item)

# # for item in dict.keys():
# #     print(item,end="\t")
# #     print(dict[item])
# #
# # for item in dict:
# #     print(item,end="\t")
# #     print(dict[item])
# #
# print("z" in dict)

########################################################        sorting a dictionary
# dict={1:'a',3:'b',2:'d',4:'c'}
# print(dict)
# i=dict[1]
#
# for item in sorted(dict.values()):
#     print(item)
# #
############################################################        iterating a dictionary

# for i1,i2 in dict1.items():
#     print(i1,"-",i2)


###########################################################            cocatenate

# dict2={5:100,6:250}
# dict3={12:'sd',123:12312}

#
# for item in (dict2,dict3): dict1.update(item);
# print(dict1)

##########################################################3                  finding the sum of keys and values

# print(sum(dict2.keys()))
# print(sum(dict2.values()))
#
# ##############################################################               multiplying all the items

# result=1
# for key,value in dict2.items():
#     result=result*value
# print(result)

##########################################                                  to remove a key

# if 12 in dict3:
#     del dict3[12]
# print(dict3)




##########################################################            adding a key to a dictionary
# dict3.update({111:'frf'})
# print(dict3)
#
# ###########################################################             print a dictionary where keys are b|w 1 and 15
#                                                           #              and values are squares of keys
# d=dict()
# for i in range(1,16):
#     d[i]=i*i
# print(d)
#############################################################            merging two dictionaries

# d=dict3.copy()
# print(d)
# d.update(dict2)
# print(d)