a=int(input())
b=int(input())
c=int(input())
if((a>b and a<c)or(a<b and a>c)):
    print("middle",a)
elif((b>a and b<c)or(b<a and b>c)):
    print("middle",b)
else:
    print("middle",c)

a=10
b=13
c=20
d=[a,b,c]
t=max(d)
d.remove(t)
print(max(d))