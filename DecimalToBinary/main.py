#Logical
n1=int(input())
n=n1
s=0
dig=1
while (n>0):
    s+=n%2*dig
    n=n//2
    dig*=10
print(s)

#functional
s=bin(n1)
print(s,type(s))
s=int(s[2:])
print(s,type(s))