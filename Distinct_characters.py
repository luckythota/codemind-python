s=input()
n=list(s.lower())
b=[]
for i in s:
    if n.count(i)==1 and i!=' ':
        b.append(i)
        v=sorted(b)
print(''.join(v))
        
    