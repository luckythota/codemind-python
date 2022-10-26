n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
l=[]
flag=0
for i in a:
        l.append(a.count(i))
v=set(l)
k=max(v)
for i in a:
    g=a.count(i)
    if k==g:
        print(i)
        break
    
