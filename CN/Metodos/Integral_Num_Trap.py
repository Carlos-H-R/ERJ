import numpy as np
# array = [0.961, 0.996, 0.995, 0.958, 0.887, 0.784, 0.653]

def error(found, original):
    if original != 0:
        return (abs(found - original)/abs(original))
    
    else:
        print("\nDivisao por Zero!\n")
        return np.NAN


def integral_trap(f,a,b,n):
    h = (b - a)/n
    integral = f(a)

    for i in range(1,n):
        integral += 2 * f(a+(h*i))
    
    integral += f(b)
    integral *= h/2

    return integral


def integral_trap_tab(f,x,y):
    if (len(x) == len(y)):
        n = len(x)    

        h = x[1] - x[0]
        integral = y[0] + y[-1]

        for i in range(1,n-1):
            integral += 2 * y[i]

        integral *= h/2

        return integral
    
    else:
        print("Erro! Vetores de tamanhos diferentes!")


def f(t):
    return ((t ** 3))


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
np.set_printoptions(precision=5)
print("Integral = ",result)


# # Erro Relativo
# original = 1.6488 # <-- Colocar aqui o valor original
# print("Erro Relativo = ",error(result,original))
