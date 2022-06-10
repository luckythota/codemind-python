n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,len(a)):
    for j in range(0,a[i]+1):
        if(a[i]==j*j):
            sum=sum+a[i]
print(sum)
      