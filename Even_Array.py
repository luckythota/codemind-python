n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    if(a[i]%2==0):
        count=count+1
if(count==n):
    print('True')
else:
    print('False')