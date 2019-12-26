list1 = ["string", 0, 3, 2, [1, 2, 3], 'a']
print(list1[0])
print(list1[3])
list2 = list1+[4, 5, 6]
list3 = list2*3
print(list2)
print(list3)
print(list1[0]*3)
print(5 in list1)
print(list1[2]//1.5)

if 2 not in list1:
    print(list1[3])

list1.append(5)
print(list1)

print(len(list1))

index=6
list1.insert(2, "is fun")
print(list1)

print(list1.index("a"))

numbers=list(range(3,20,3))
print(numbers)
