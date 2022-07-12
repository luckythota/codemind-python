n=int(input())
a=list(map(int,input().split()))
flag=0
k=[]
for i in a:
    if a.count(i)==i and i not in k:
        k.append(i)
        flag=1
if flag==1:
    print(*k)
if flag==0:
    print('-1')