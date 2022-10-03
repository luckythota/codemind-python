n=int(input())
a=list(map(int,input().split()))
l=[]
flag=0
for i in a:
    if i%2==0:
        l.append(i)
for i in l:
    if len(l)>=2:
        flag=1
if flag==1:
    print('1')
else:
    print('0')
