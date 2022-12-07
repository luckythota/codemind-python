n=int(input())
a=list(map(int,input().split()))
l=[]
m=[]
v=[]
for i in range(0,n,2):
    l.append(a[i])
for i in range(1,n,2):
    m.append(a[i])
for i in range(0,len(l)):
    for j in range(0,m[i]):
        v.append(l[i])
print(*v)