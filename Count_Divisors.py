l,r,k=list(map(int,(input()).split()))
count=0
i=l
for i in range(l,r+1,1):
    if(i%k==0):
        count=count+1
print(count)