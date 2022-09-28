s1=input()
s2=input()
v=list(s1.lower())
n=list(s2.lower())
l=[]
k=[]
flag=0
for i in v:
    if i in n and i!=' ':
        l.append(i)
for i in l:
    if i not in k:
        k.append(i)
        flag=1
g=sorted(k)
if flag==1:
    print(''.join(g))
else:
    print('-1')

