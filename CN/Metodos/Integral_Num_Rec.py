import numpy as np


# Calcula o erro
def error(found, original):
    if original != 0:
        return (abs(found - original)/abs(original))
    
    else:
        print("\nDivisao por Zero!\n")
        return np.NAN


def intg_rec(xs, ys, met):
    
    integral = 0
    n = len(xs)-1
    # h = xs[1] - xs[0]

    for i in range(n):
        if met == 'l':
            integral = (xs[i+1] - xs[i]) * ys[i]
        
        elif met == 'r':
            integral = (xs[i+1] - xs[i]) * ys[i+1]
        
        elif met == 'm':
            integral = (xs[i+1] - xs[i]) * ((ys[i] + ys[i+1]) / 2)

    return integral


# Entrada de dados
x = list(map(float, input().split()))
y = list(map(float, input().split()))
metodo = map(str,input()) 


# Processamento
integral = intg_rec(x,y,metodo)

# Saida de dados
np.set_printoptions(precision=4)
print("Valor da Integral = ",integral)