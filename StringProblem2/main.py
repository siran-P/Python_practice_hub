st='abhjkez92163'
j=[]
c=[]
for i in range(len(st)):
    if st[i].isdigit():
        j.append(st[i])
    else:
        c.append(st[i])
j.sort()
j=j[::-1]
c.sort()
for i in range(len(c)):
    if c[i]=='z':
        c[i]='a'
    else:
        c[i]=chr(ord(c[i])+1)
for i in range (len(j)):
    j[i]=chr(ord(j[i])-1)
print(*c,*j,sep='') 

