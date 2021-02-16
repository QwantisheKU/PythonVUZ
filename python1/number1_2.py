import math
def f12(x):
    if x < 75:
        return 67*(x**8+math.sin(x))**4-abs(x)
    elif 75 <= x < 135:
        return math.sin(24*x**5)-math.cos(x)
    elif 135 <= x < 169:
        return abs(90*x**4-94*x**5+73)-math.cos(30*x**7+x**4)
    else:
        return math.log(18*x**3)+43*x**5