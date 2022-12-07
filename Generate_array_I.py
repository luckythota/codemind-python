n=int(input())
a=list(map(int,input().split()))
l=[]
m=[]
v=[]
for i in range(0,n):
    if i%2==0:
        l.append(a[i])
    if i%2!=0:
        m.append(a[i])
for i in range(0,len(m)):
    for j in range(0,m[i]):
        v.append(l[i])
print(*v)