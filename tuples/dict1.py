# line="hello hai hello hai how"
# words=line.split(" ")
# print(words)
# dict={}
#
# for word in words:
#     if word not in dict:
#         dict[word]=1
#     else:
#         dict[word]+=1
#
# print(dict)


line="cbaba"
for da in line:
    print(da)
dict={}
for i in line:
    if i not in dict:
        dict[i]=1
    else:
        print(i,"is the recursing character")
        break
print(dict)


