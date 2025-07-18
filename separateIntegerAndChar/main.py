x='abc327ij'
c=0
n=''
for i in x:
    if i<='9' and i>='0':
        c=c+int(i)
    else:
        n=n+i
print(c)
print(n)