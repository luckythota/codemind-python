a,b,c=list(map(int,(input()).split()))
s=(a+b+c)/2.0
area=s*(s-a)*(s-b)*(s-c)
import math
e=math.sqrt(area)
print('%.2f' %e)