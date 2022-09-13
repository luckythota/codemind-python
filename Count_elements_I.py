m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
m=[]
for i in a:
    if i in b:
        l.append(i)
for i in l:
    if i not in m:
        m.append(i)
    else:
        flag=1
print(len(m))