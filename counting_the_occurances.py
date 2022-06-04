s=input()
c=input()
count=0
flag=0
for i in s:
    if(i==c):
        count=count+1
        flag=1
if(flag==1):
    print(count)
else:
    print('-1')