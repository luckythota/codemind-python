s1=input()
s2=input()
v=list(s1.lower())
n=list(s2.lower())
l=[]
k=[]
for i in v:
    if i not in n and i!=' ':
        l.append(i)
for i in n:
    if i not in v and i!=' ':
        l.append(i)
for i in l:
    if i not in k:
        k.append(i)
g=sorted(k)
print(''.join(g))