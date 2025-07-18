def loop():
    x=int(input())
    l=[]
    for i in range(1,x+1):
        l.append(i)
    return l
def power():
    x=int(input("x:"))
    y=int(input("y:"))
    return x**y
def hexa():
    x=int(input("x:"))
    h=hex(x)[2:]
    return h
#c=int(input("Enter choice:\n1.print 1 to n\n2.x power y\n3.Decimal to hexadecimal\n"))
while 1:
    c=int(input("\n1.print 1 to n\n2.x power y\n3.Decimal to hexadecimal\nEnter choice:"))
    match(c):
        case 1:print(*loop())
        case 2:print(power())
        case 3:print(hexa())
        case 4:
            print("Exit")
            break
        case _:
            print("Invalid")