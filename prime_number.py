n=int(input())
i=2
count=0
for i in range(i,n,1):
    if(n%i==0):
        count=count+1
if(count==0):
    print('prime')
else:
    print('not a prime')