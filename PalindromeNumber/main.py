n1=int(input())
n=str(n1)
r=n[::-1]
print(n,r)
if(n==r):
    print('Palindrome')
else:
    print('Not Palindrome')