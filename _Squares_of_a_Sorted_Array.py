n=int(input())
a=list(map(int,input().split()))
v=[]
for i in range(0,n):
    v.append(a[i]*a[i])
g=sorted(v)
print(*g)