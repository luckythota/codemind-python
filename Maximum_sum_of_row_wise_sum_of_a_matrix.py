m,n=map(int,input().split())
b=[]
l=[]
for i in range(0,m):
    a=list(map(int,input().split()))
    b.append(a)
    v=sum(a)
    l.append(v)
print(max(l))