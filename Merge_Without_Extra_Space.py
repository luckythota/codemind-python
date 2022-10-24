t=int(input())
for i in range(t):
    v=[]
    m,n=map(int,input().split())
    l=list(map(int,input().split()))
    k=list(map(int,input().split()))
    for i in l:
        v.append(i)
    for j in k:
        v.append(j)
    g=sorted(v)
    print(*g)
    