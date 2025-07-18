l=[1,3,3,7,8,6]
d=[]
for i in l:
    if i not in d:
        d.append(i)
print(d)
d.sort()
print(d)


b={1,3,3,7,8,6}
print(sorted(b))