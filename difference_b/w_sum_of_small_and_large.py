s=input()
a=s.split(" ")
sum=0
sum1=0
for i in a:
    u=min(i)
    sum=sum+ord(u)
    v=max(i)
    sum1=sum1+ord(v)
print(sum1-sum)
    