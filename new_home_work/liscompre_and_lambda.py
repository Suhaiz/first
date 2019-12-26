
print((lambda a,b,exp:[eval('+'.join(str(i)+exp for i in range(int(a),int(b)+1)))])(*input().split()))

# print(f(1,4,'*2'))