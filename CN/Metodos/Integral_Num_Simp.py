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
        integral = 0.0

        x1=a
        x2=a+h
        x3=a+2*h

        for i in range(0,n,2):
            integral += f(x1) + f(x3)
            integral += 4 * f(x2)

            x1 += 2*h
            x2 += 2*h
            x3 += 2*h

        integral *= h/3
        return integral
    
    else:
        print('\nO valor de n deve ser par!\n')
        return np.NAN
    

def simp_1_3_tab(xs,ys):
    if (len(xs) != len(ys)):
        raise ValueError("Vetores X e Y devem ter o mesmo tamanho!")
    
    n = len(xs) - 1
    if (n % 2 == 0):
        h = (xs[-1] - xs[0])/n
        integral = 0.0

        for i in range(0,n,2):
            integral += ys[i] + ys[i+2]
            integral += 4 * ys[i+1]

        integral *= h/3
        return integral
    
    else:
        print('\nO valor de n deve ser par!\n')
        return np.NAN



def simp_3_8(f,a,b,n):
    if (n % 3 == 0):
        h = (b - a)/n
        integral = f(a) + f(b)

        for i in range(1,n):
            x = a + i*h

            if (i%3 == 0):
                integral += 2 * f(x)

            else:
                integral += 3 * (x)

        integral *= 3*h/8
        return integral

    else:
        print('\nO valor de n deve ser multiplo de 3\n')
        return np.NAN


def simp_3_8_tab(xs,ys):
    if (len(xs) != len(ys)):
        raise ValueError("Vetores X e Y devem ter o mesmo tamanho!")
    
    n = len(xs) - 1
    if (n % 3 == 0):
        h = (xs[-1] - xs[0])/n
        integral = ys[0] + ys[-1]

        for i in range(1,n):
            if (i%3 == 0):
                integral += 2 * ys[i]

            else:
                integral += 3 * ys[i]

        integral *= 3*h/8
        return integral

    else:
        print('\nO valor de n deve ser multiplo de 3\n')
        return np.NAN


def f(t):
    return (np.sin(t))


# # Input for Simpson 1/3
# a = float(input())
# b = float(input())
# n = int(input())
# result = simp_1_3(f,a,b,n)


# # Input for Simpson 1/3 Table
# x = list(map(float,input().split()))
# y = list(map(float,input().split()))
# result = simp_1_3_tab(x,y)


# # Input for Simpson 3/8
# a = float(input())
# b = float(input())
# n = int(input())
# result = simp_3_8(f,a,b,n)


# Input for Simpson 3/8 Table
x = list(map(float,input().split()))
y = list(map(float,input().split()))
result = simp_3_8_tab(x,y)


# Output
# np.set_printoptions(precision=11)
print("Integral = ",result)

# # Erro Relativo
# original = 1.6488 # <-- Colocar aqui o valor original
# print("Erro Relativo = ",error(result,original))
