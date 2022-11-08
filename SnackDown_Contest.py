t=int(input())
for i in range(0,t):
    v=[]
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(0,len(a)):
        v.append(a[i])
    for i in range(0,len(b)):
        v.append(b[i])
    k=set(v)
    g=len(k)
    if g==n:
        print('YES')
    else:
        print('NO')
    