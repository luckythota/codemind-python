s=input()
count=0
for i in s:
    if i in 'aeiouAEIOU':
        count=count+1
    if(i==' '):
        print(count,end=' ')
        count=0
print(count)