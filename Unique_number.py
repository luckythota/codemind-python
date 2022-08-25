n=int(input())
a=[]
flag=0
while(n>0):
    r=n%10
    a.append(r)
    n=n//10
for i in a:
    if a.count(i)>1:
        flag=1
        break
if flag!=1:
    print('Unique Number')
else:
    print('Not Unique Number')