storage={}
reasons=set()
test=()


# print(type(reasons))
# print(type(storage))

month=['jan','feb','mar','jan']


for item in month:
    if item not in storage:
        storage[item]=dict()

print(storage)
storage['jan']['oth']=25000
storage['feb']['ent']=10000
print(storage)

print(storage['feb']['ent'])