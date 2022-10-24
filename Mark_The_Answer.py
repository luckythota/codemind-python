m,n=map(int,input().split())
#reading no. of questions and max. difficulty
a=list(map(int,input().split()))
#reading list
c=0
#make count=0
for i in range(0,m):
#loop running from 0 to m no. of elements
    if a[i]>=n:
    #check the condition wheather n element is greater than or equal to array elements
        c+=1
    #increment count
print(c)
#print count