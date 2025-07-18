#ip='abcdefgha' op=hhhhhhhh 8
#ip='qrcykvxcryxx' op=yyyyyyyyy 9
#ip='fghnettefynk' op=ttttttttttt 11
st='fghnettefynk'
ma=max(st)
mi=min(st)
n=0
for i in range(len(st)):
    if st[i]==mi:
        n+=i
print(n*ma,n)
