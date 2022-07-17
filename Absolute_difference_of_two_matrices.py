import math
r1=int(input())
a=[]
for i in range(r1):
    l=list(map(int,input().split()))
    a.append(l)
b=[]
for j in range(r1):
    m=list(map(int,input().split()))
    b.append(m)
res=[[abs(a[i][j]-b[i][j])for j in range(r1)]for i in range(r1)]
for i in res:
    print(*i)
        