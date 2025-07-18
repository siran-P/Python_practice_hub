#i/p=5 1 2 2 3 7 o/p=[1,3,7]   i/p=6 2 2 2 3 3 18 o/p=[18]

#My method
n=int(input())
l=[]
l2=[]
for i in range(n):
    a=int(input())
    if a in l:
        l2.append(a)
    else:
        l.append(a)
for i in l2:
    if i in l:
        l.remove(i)
print(l)

#Sir method
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
r=[]
for i in a:
    if(a.count(i)==1):
       r.append(i)
print(r)