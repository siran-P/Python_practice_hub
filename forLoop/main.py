n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
for i in range(n1,n2+1):#n1 to n2
    print(i)

n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
for i in range(n1+1):#0 to n1
    print(i)

n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
for i in range(n2,n1,-1):#n2 to n1-1
    print(i)

n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
n3=int(input("Enter n3:"))
for i in range(n1,n2,n3):#n1 ,n1+n3 ,+n3...to n2
    print(i)

n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
for i in range(n1,n2):#n1,n1+1,n1+2,....,n2
    print(i,end=",")
print(n2)


n=int(input())
for i in range(n):
    for j in range(1,n+1):#1 2 3 .. n
        print(j,end=' ')  #1 2 3 .. n
    print()