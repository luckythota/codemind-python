t=int(input())
X=0
for i in range(t):
    s=input()
    if s=='++X' or s=='X++':
        X+=1
    else:
        X-=1
print(X)
        