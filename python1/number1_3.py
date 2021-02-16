import math
def f13(n, m):
    summa1 = 0
    summa2 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            summa1 += (math.exp(j)-abs(j)-99)
    for i in range(1, n+1):
        summa2 += (i**4/61-12*i**5-19)
    return summa1 + summa2
