st='cxhyb24k'
l1=[]
l2=[]
for i in st:
    if i>='0' and i<='9':
        l1.append(int(i))
    else:
        l2.append(i)
print(max(l1)*min(l2),end='')