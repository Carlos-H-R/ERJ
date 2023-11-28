import numpy as np
# array = [0.993252, 1.202972, 1.376244, 1.52388, 1.652497, 1.766442, 1.868721]

def error(found, original):
    if original != 0:
        return (abs(found - original)/abs(original))
    
    else:
        print("\nDivisao por Zero!\n")
        return np.NAN


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


def simpson_1_3(f, a, b, n):
    """
    Calcula a integral definida de uma função f(x) no intervalo [a, b] usando o método 1/3 de Simpson.

    :param f: A função a ser integrada.
    :param a: O limite inferior do intervalo.
    :param b: O limite superior do intervalo.
    :param n: O número de subintervalos. Deve ser um número par.
    :return: O valor da integral aproximada ou NaN em caso de erro.
    """
    try:
        if n % 2 != 0:
            raise ValueError("O número de subintervalos (n) deve ser par.")

        h = (b - a) / n
        x = [a + i * h for i in range(n + 1)]
        y = [f(xi) for xi in x]

        integral = y[0] + 4 * sum(y[i] for i in range(1, n, 2)) + 2 * sum(y[i] for i in range(2, n - 1, 2)) + y[n]
        integral *= h / 3

        return integral
    except Exception as e:
        print(f"Erro: {str(e)}")
        return float(np.nan)


def simp_1_3_New():
    pass


def f(t):
    return ((t**2))


# Input
a = float(input())
b = float(input())
n = int(input())
result = simpson_1_3(f,a,b,n)


# Output
np.set_printoptions(precision=5)
print("Integral = ",result)

# # Erro Relativo
# original = 1.6488 # <-- Colocar aqui o valor original
# print("Erro Relativo = ",error(result,original))
