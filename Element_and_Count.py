n=int(input())
a=list(map(int,input().split()))
f=[None]*len(a)
visited=-1
for i in range(0,len(a)):
    c=1
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            c+=1
            f[j]=visited
    if f[i]!=visited:
        f[i]=c
for i in range(0,len(f)):
    if f[i]!=visited:
        print(str(a[i]),str(f[i]),end=' ')
        