s=(input())
count=0
for i in s:
    if i in '0123456789':
        count=count+1
if(count>0):
    print('Contains',count,'digit')
else:
    print("Doesn't contain digit")
    