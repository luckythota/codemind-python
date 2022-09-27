n=int(input())
l=list(map(int,input().split()))
a=[]
k=[]
for i in l:
    v=len(str(i))
    a.append(v)
k.append(max(a))
c=0
for i in a:
    if i in k:
        c+=1
print(c)