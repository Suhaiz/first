stacc=[]
top=0
b=int(input("enter the size\t"))

def insrt(a):
    global top
    top=0
    stac=[]
    for i in range(0,a):
        e=int(input("enter the element\t"))
        if(top<a):
            stac[top]=e
            top+=1
        elif(top==a):
            print("stack is full\t")
    return stac

stacc=insrt(b)
print(stacc)
