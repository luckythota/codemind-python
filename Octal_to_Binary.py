t=int(input())
for i in range(t):
    s=input()
    n=int(s,8)
    b=bin(n)
    k=b.replace('0b','')
    print(k)