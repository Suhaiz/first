str=input("enter your string\t")
lst=[]
flag=False
for i in range(0,len(str)):
    if flag:
        break
    for j in range(0,len(str)):
        if i!=j:
            if str[i]==str[j]:
                print("\nthe first recursive character is",str[i])
                flag=True
                break
