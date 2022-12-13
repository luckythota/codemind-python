t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    k=list(s)
    for i in range(n):
        if k.count(k[i])==1:
            print(k[i])
            break
    else:
        print('-1')