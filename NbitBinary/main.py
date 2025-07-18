n=int(input("Enter decimal no:"))
nb=int(input("Enter No of bits:"))
a=bin(n)
a=a[2:]
x=len(a)
a=((nb-x)*"0")+a
print(a)
