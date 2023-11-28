import numpy as np


def simp_1_3(f,a,b,n):
    if (n % 2 == 0):
        h = (b - a)/n
        integral = 0

        x1=a
        x2=a+h
        x3=a+2*h

        for i in range(n-2):
            integral += f(x1) + f(x3)
            integral += 4 * f(x2)

            x1 += 2*h
            x2 += 2*h
            x3 += 2*h

        integral *= h/3

    return integral


def simp_1_3_New():
    pass


def f(t):
    return t**3


# Input
a = float(input())
b = float(input())
n = int(input())
result = simp_1_3(f,a,b,n)


# Output
np.set_printoptions(precision=4)
print("Integral = ",result)
