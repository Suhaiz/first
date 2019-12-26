# print(lambda no:cuube==str(no**3),no+ "is trimorphic" if cuube[len(cuube)-1]==no else "not")(input())

no=int(input())
cube=str(no**3)
if int(cube[-len(str(no)):])==no:
    print(str(no)+" is trimorphic")
else:
    print(str(no)+ " is not trimorphic")




#################start stop step
# cube="15438249"
# print(cube[-3:])