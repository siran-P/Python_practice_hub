a=[]
a.append(50)
a.append(4)
a.append(29)
print(a)
a.insert(0,31)#insert(index,value)
print(a)
a.insert(55,55)#indext out of bound means it will add at last
print(a)
a.remove(4)
print(a)

a=[10,20]
b=[10,20,30]
print(a+b)