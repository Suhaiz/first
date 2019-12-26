from math import pi as si
print(si)

st=set()
print(type(st))
st1={1}
print(type(st1))
st2={}
print(type(st2))

def mainfunc(a,b):
    return a+b

def newfunction(func,z,x):
    return(func(z,x),func(z,x))

a=23
b=24
print(newfunction(mainfunc,a,b))