#i/p=5 3 2 4 1 1 0   i/p2=3 3 5 2 2 6
#o/p=20              o/p=44

l=[]
a=-1
s=0
while a!=0:
    a=int(input())
    if(a%2==0):
        s=s+a**2
    l.append(a)
print(l,'->',s)
    