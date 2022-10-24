m=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
v=sorted(a)
g=sorted(b)
if v==g:
    print('True')
else:
    print('False')