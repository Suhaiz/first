from statistics import median

f1= open("/home/suhaiz/PycharmProjects/luminarpython/new_home_work/para_text")
storage={}
reason=()
amounts=[]
normal_amounts=[]
reasons=set()
for line in f1:
    month,reason,amount,postfix=line.rstrip("\n").split(" ")
    print(month,reason,amount,postfix)
    amount=int(amount)

    if postfix=='B':
        amount*=10**9
    if postfix=='K':
        amount*=10**3
    if postfix=='M':
        amount*=10**6

    if month not in storage:
        storage[month]=dict()
    storage[month][reason]=amount

    reasons.add(reason)
for reason in reasons:

    amounts=[storage[month][reason] for month in storage]

    normal_amounts=median(amounts)

    bad_month=[month for month in storage if storage[month][reason]!=normal_amounts]

#
# for month in bad_month:
#     print("month '{}' has a problem with amount for reason '{}'. provided value is '{}',however {} is expected".format(month,reason,storage[month][reason],normal_amounts))
print(bad_month)
# print(normal_amounts)

# print(amounts)
# print(storage)
#
#
# print(bad_month)