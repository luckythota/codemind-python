n=int(input())
a=list(map(int,input().split()))
b=[]
flag=0
for i in a:
    if a.count(i)==1:
        b.append(i)
        flag=1
if flag==1:
    print(max(b))
else:
    print('-1')
    