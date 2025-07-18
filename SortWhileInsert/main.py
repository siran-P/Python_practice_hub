n=int(input())
l=[]
for i in range(n):
    a=int(input())
    for j in range(len(l)):
        if(l[j]>a):
            l.insert(j,a)
            break
    else:
        l.append(a)
print(l)