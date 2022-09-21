t=int(input())
for i in range(t):
    a=int(input())
    b=bin(a)
    c=b.replace("0b","")
    print(c)