# PRIME NUMBER
from math import sqrt


def primenumber(X):
    Sum=int(0)
    for i in range(sqrt(X)):
        if X % i == 0:
            Sum=Sum+i

    if Sum==1:
        return "ist prime"


# BAKHSH PAZIRI

def bakhshpazir(X,Y):
    if X%Y==0
        print('bakhshpazire')
    else:
        print ('nist')


#ADADE GHABLE UN ADAD
def ADAD(X):
    for i in range(X):
        print(i)



#SAL kabise
def leapyear(Y,D,M):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 31, 30, 31, 30]
    days_passed = 0
    if Y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        days[1] = 29
    for months in days[:m - 1]:
        days_passed += months
    days_passed += d
    return days_passed

