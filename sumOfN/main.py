n=int(input())
s=0
for i in range(1,n):
    print(i,end='+')
    s=s+i
s+=n
print(n,'=',s)