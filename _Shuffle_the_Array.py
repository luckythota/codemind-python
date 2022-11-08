m=int(input())
a=list(map(int,input().split()))
n=int(input())
l=[]
v=[]
k=[]
for i in range(0,n):
    l.append(a[i])
for j in range(n,m):
    v.append(a[j])
for i in range(0,len(l)):
    for i in range(0,len(v)):
        print(l[i],v[i],end=' ')
    break
