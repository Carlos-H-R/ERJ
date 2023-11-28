import numpy as np


def integral_trap(f,a,b,n):
    h = (b - a)/n
    integral = f(a) + f(b)

    for i in range(1,n):
        integral += 2 * f(a+(h*i))
    
    integral *= h/2

    return integral


def integral_trap_tab(f,x,y):
    if (len(x) == len(y)):
        n = len(x)    

        h = x[1] - x[0]
        integral = y[0] + y[n]

        for i in range(1,n-1):
            integral += 2 * y[i]

        integral *= h/2

        return integral
    
    else:
        print("Erro! Vetores de tamanhos diferentes!")


def f(t):
    return t**3


# # Input Tabelado
# xs = list(map(float,input().split()))
# ys = list(map(float,input().split()))
# result = integral_trap_tab(f,xs,ys)

# Input Intervalo
a = float(input())
b = float(input())
n = int(input())
result = integral_trap(f,a,b,n)

# Output
np.set_printoptions(precision=4)
print("Integral = ",result)
