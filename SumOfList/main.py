n1=int(input())
l1=[]
for i in range(n1):
    l1.append(int(input()))
n2=int(input())
if n1!=n2:
    print("Invalid")
else:
    l2=[]
    for i in range(n2):
        a=int(input())
        l2.append(l1[i]+a)
    print(l2)

    