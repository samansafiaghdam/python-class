from math import  sqrt
def fasele(p1,p2):
    return sqrt(((p1.x)-(p2.x))**2+((p1.y)-(p2.y))**2)

class coordinate:
    x=0
    y=0

p1=coordinate()
p2=coordinate()
p1.x=int(input())
p2.x=int(input())
p1.y=int(input())
p2.y=int(input())
a=fasele(p1,p2)
print(a)

