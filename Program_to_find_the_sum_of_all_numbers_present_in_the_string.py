s=input()
sum=0
for i in s:
    if i in '0123456789':
        sum=sum+int(i)
print(sum)