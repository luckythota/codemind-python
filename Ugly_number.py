n=int(input())
flag=0
while n%2==0:
    n=n//2
if n==1:
    flag=1
while n%3==0:
    n=n//3
if n==1:
    flag=1
while n%5==0:
    n=n//5
if n==1:
    flag=1
if flag==1:
    print('Ugly Number')
else:
    print('Not Ugly Number')
