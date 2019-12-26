maxi=int(input("enter the maximum integer\t"))
possibleprime=2

while possibleprime<maxi+1:
    isprime=True
    num=2
    while num<possibleprime:
        if possibleprime%num==0:
            isprime=False
            break
        num+=1

    if isprime:
        print(possibleprime)
    possibleprime+=1