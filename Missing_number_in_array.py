t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(1,n+1):
        if j not in a:
                print(j)
                break