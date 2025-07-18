tot=int(input())
room=int(input())
maxi=int(input())
for i in range (1,room+1):
    if(tot>maxi):
        print(maxi)
        tot=tot-maxi
    else:
        print(maxi)