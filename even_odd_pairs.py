n=int(input())
a=list(map(int,input().split()))
l=[]
m=[]
for i in range(0,n):
    if a[i]%2==0:
        l.append(a[i])
    if a[i]%2!=0:
        m.append(a[i])
v=[]
i,j=0,0
while(i<len(l) or j<len(m)):
    if i<len(l):
        v.append(l[i])
    i+=1
    if j<len(m):
        v.append(m[j])
    j+=1
if len(v)%2!=0:
    v.append(0)
print(*v)
