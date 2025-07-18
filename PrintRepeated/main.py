a=[1,2,2,3,4,5,6,6]
l=[]
for i in a:
    if(a.count(i)>1 and i not in l):
        l.append(i)
        print(i)