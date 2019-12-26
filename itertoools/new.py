# import itertools
# #
#
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

print(type(people))
#
def get_state(person):
    return person['state']

a=get_state
print(a)
# result=itertools.groupby(people,get_state)
#
#
# # result=itertools.groupby(people,lambda person:person['state'])
#
# for key,group in result:
#     for i in group:
#         print(i)
#     print(key,len(list(group)))
#

#
# lst= [{1:'i',2:'love',3:'you'},{4:'love'},{5:'love'}]
# print(lst['love'])
