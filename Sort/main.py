n=int(input())
l=[]
res=[]
for i in range(n):
    l.append(int(input()))
for i in range(n):
    res.append(min(l))
    l.remove(min(l))
print(res)