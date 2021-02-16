import math
def f14(n):
    if n == 0:
        return 2
    else:
        return abs(f14(n-1))-1/43*f14(n-1)
