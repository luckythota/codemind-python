n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    v=len(str(i))
    l.append(v)
k=max(l)
for i in range(0,len(l)):
    if l[i]==k:
        print(a[i],end=' ')
