s=input()
a=s.split(" ")
import math
for i in a:
    sum=0
    sum1=0
    u=min(i)
    v=max(i)
    sum=sum+ord(u)
    sum1=sum1+ord(v)
    print(abs(sum-sum1),end=' ')
    