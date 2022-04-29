n=int(input())
i=1
sum=0
m=n
for i in range(i,m,1):
    if(m%i==0):
        sum=sum+i
if(sum>m):
    print('True')
else:
    print('False')
    