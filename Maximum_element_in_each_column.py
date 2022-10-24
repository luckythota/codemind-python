m,n=map(int,input().split())
b=[]
for i in range(m):
    a=list(map(int,input().split()))
    b.append(a)
for i in range(0,n):
    l=[]
    for j in range(0,m):
        l.append(b[j][i])
    print(max(l))
        