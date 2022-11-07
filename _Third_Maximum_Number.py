n=int(input())
a=list(map(int,input().split()))
k=set(a)
v=sorted(k)
if n<3:
    print(max(k))
else:
    print(v[len(k)-3])