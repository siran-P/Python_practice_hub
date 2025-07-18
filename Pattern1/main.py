n=int(input("Enter:"))
#Normal method
for i in range(1,n+1):
    for j in range(i):
        print("* ",end='');
    print()
    
#Single loop
for i in range(1,n+1):
    print(i*"* ")