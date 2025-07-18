l=[1,3.0,17.7,78.5,9,62.5,9,22]
j=[]
f=[]
for i in l:
    if type(i)==int:
        j.append(i)
    else:
        f.append(i)
print(j)
print(f)

# a=5
# print(type(a),a)
# a=a/1
# print(type(a),a)