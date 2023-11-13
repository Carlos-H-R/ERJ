import numpy as np


# Calcula o erro
def error(found, original):
    if original != 0:
        return (abs(found - original)/abs(original))
    
    else:
        print("\nDivisao por Zero!\n")
        return np.NAN
    

def intg_rec(f,a,b,n,m):
    integral = 0
    h = (b-a)/n

    for i in range(n):
        if m == 'l':
            integral += f(a + i*h) * h
        
        elif m == 'r':
            integral += f(a + (i+1)*h) * h
        
        elif m == 'm':
            integral += f(a + (i + 0.5)*h) * h

    return integral

def intg_rec_tab(xs, ys, met):
    
    integral = 0
    n = len(xs)-1
    # h = xs[1] - xs[0]

    for i in range(n):
        if met == 'l':
            integral += (xs[i+1] - xs[i]) * ys[i]
        
        elif met == 'r':
            integral += (xs[i+1] - xs[i]) * ys[i+1]
        
        elif met == 'm':
            integral += (xs[i+1] - xs[i]) * ((ys[i] + ys[i+1]) / 2)

    return integral


# Define f(x) -> só alterar a funcao abaixo
def f(x):
    return ((x**2) * np.tan(x))


# Entrada de dados -> funcao
a, b, n, m = input().split()
a = float(a)
b = float(b)
n = int(n)
m = str(m)


# # Entrada de dados -> Tabela
# x = list(map(float, input().split()))
# y = list(map(float, input().split()))
# metodo = map(str,input()) 


# Processamento
# integral = intg_rec_tab(x,y,metodo)
integral = intg_rec(f,a,b,n,m)

# Saida de dados
np.set_printoptions(precision=5)
print("Valor da Integral = ",integral)


"""
Quando usando tabela valores o input é lista de valores de x na primeira linha
                                       lista de valores de y na segunda

Quando usando funcao o input é:
    limite_inferior     limite_superior     numero_de_intervalos    metodo
"""