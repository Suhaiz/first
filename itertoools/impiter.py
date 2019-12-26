import itertools


############################################################# first will learn the count function
# lst=[100,200,300,400]
# counter=itertools.count(start=0.2,step=2)

# print(next(counter))
# print(next(counter))
# print(next(counter))

# daily_data=list(zip(itertools.count(),lst))               ###we will pass the function and iterable just like for map function

# daily_data1=list(zip(itertools.count(start=1,step=1),lst))
#
# print(daily_data)
# print(daily_data1)
#
#
# ###################################################### now lets learn the repeat function
#

# counter=itertools.repeat(2,times=3)
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

##################################################### star map


# sq=list(itertools.starmap(pow,[(3,2),(1,2),(2,2)]))
# print(sq)

################################################### combinations
#
letters=['a','b','c','d']
result=itertools.combinations(letters,3)
for item in result:
    print(item)
print("\n\n")
################################################3  permutations
letters=['a','b','c','d']
result=itertools.permutations(letters,3)
for item in result:
    print(item)
print("\n\n")
#

#############################################  product
#
letters=['a','b','c','d']
result=itertools.product(letters,repeat=3)
for item in result:
    print(item)


###################################### chain function which is used to combine three lists

# letters=[1,2,3,4]
# names=[4,5,6]
# heloo=[7,8,9]
#
# combined=itertools.chain(letters,names,heloo)
# for item in combined:
#     print(item)

######################################3 slice

# result=itertools.islice(range(10),1,5)
#
# for item in result:
#     print(item)
#
#
# result=itertools.islice(range(10),1,5,2)
#
# for item in result:
#     print(item)

################################# compress

# letters=['a','b','c','d']
# selectors=[True,False,True,False]
# result=itertools.compress(letters,selectors)
#
# for item in result:
#     print(item)


# letters=['a','b','c','d']
# selectors=[1,0,1,0]
# result=itertools.compress(letters,selectors)
#
# for item in result:
#     print(item)