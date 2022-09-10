n=int(input())
v=str(n)
if v[0]=='-':
    k=int('-'+v[:0:-1])
else:
    k=int(v[::-1])
print(k)
    