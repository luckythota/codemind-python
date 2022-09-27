s=input()
v=list(s.lower())
c=0
b=[]
for i in v:
    if i!=' ':
        if i not in b:
            b.append(i)
n=sorted(b)
print(''.join(n))
    