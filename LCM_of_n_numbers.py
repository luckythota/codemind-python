def find_lcm(a,b):
    if(a>b):
        c = a
        d = b
    else:
        c = b
        d = a
    rem = c % d
    while(rem != 0):
        c = d
        d = rem
        rem = c % d
    g = d
    lcm = int(int(a * b)/int(g))
    return lcm

n=int(input())
l =list(map(int,input().split()))
 
a= l[0]
b= l[1]
lcm = find_lcm(a,b)
 
for i in range(2,n):
    lcm = find_lcm(lcm, l[i])
     
print(lcm)