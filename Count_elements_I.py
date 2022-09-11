m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in a:
    if i in b:
        l.append(i)
for i in b:
    if i in a:
        l.append(i)
v=set(l)
print(len(v))