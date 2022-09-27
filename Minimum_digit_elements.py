n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
for i in a:
    v=len(str(i))
    l.append(v)
s=min(l)
v=[]
v.append(s)
for i in l:
    if i in v:
        c+=1
print(c)
        