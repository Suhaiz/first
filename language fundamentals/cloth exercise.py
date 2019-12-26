cloth=int(input("Choose your cloth type \n1)SILK \n2)linen \n3)cotton\n\n:"))
if(cloth==1):
    pr=int(input("enter the purchase rate\n"))
    if(pr>5000):
        print("the final purchase rate is  \n",pr)
    elif(pr>4000 and pr<=5000):
        print("the final purchase rate is  \n",pr-(pr*(10/100)))
    elif(pr>3000 and pr<=4000):
        print("the final purchase rate is  \n",pr-(pr*(8/100)))
    elif(pr>2000 and pr<=3000):
        print("the final purchase rate is  \n",pr-(pr*(7/100)))
    else:
        print("the final purchase rate is  \n",pr)

elif(cloth==2):
    pr=int(input("enter the purchase rate\n"))
    if(pr>5000):
        print("the final purchase rate is  \n",pr-(pr*(20/100)))
    elif(pr>4000 and pr<=5000):
        print("the final purchase rate is  \n",pr-(pr*(10/100)))
    elif(pr>3000 and pr<=4000):
        print("the final purchase rate is  \n",pr-(pr*(9/100)))
    elif(pr>2000 and pr<=3000):
        print("the final purchase rate is  \n",pr-(pr*(7/100)))
    else:
        print("the final purchase rate is  \n",pr-(pr*(5/100)))
elif(cloth==3):
    pr=int(input("enter the purchase rate\n"))
    if(pr>5000):
        print("the final purchase rate is  \n",pr-(pr*(20/100)))
    elif(pr>4000 and pr<=5000):
        print("the final purchase rate is  \n",pr-(pr*(10/100)))
    elif(pr>3000 and pr<=4000):
        print("the final purchase rate is  \n",pr-(pr*(9/100)))
    elif(pr>2000 and pr<=3000):
        print("the final purchase rate is  \n",pr-(pr*(7/100)))
    else:
        print("the final purchase rate is  \n",pr-(pr*(5/100)))