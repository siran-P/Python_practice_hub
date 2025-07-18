# tup.append(9) or tup.insert(0,9) can't add because of immutable
# it requires less space to store values
# tuples are fater than list
tup=(1,2,3,4,5,6)
print(tup)
for i in tup:
    print(i,end=' ')