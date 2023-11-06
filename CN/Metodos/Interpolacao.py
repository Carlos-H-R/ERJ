import numpy as np


# Transforma uma lista de Float em uma lista de Pontos
def mk_point(array):
    k = len(array)

    if (k % 2 != 0):
        print("Erro! Tamanho do array é ímpar!")
        return np.NAN
        # array.append(np.NAN)
        # k += 1

    points = []
    for i in range(0,k,2):
        points.append((array[i],array[i+1]))

    return points


def mk_knots(array):
    k = len(array)

    if (k % 2 != 0):
        print("Erro! Tamanho do array é ímpar!")
        return np.NAN
        # array.append(np.NAN)
        # k += 1

    x = []
    y = []

    for i in range(0,k,2):
        x.append(array[i])
        y.append(array[i+1])

    return np.array(x),np.array(y)
        

# Calcula o resultado do polinomio usando os Coeficientes e o valor de X
def interpol_value(coef,x):
    result = 0

    for i in range(len(coef)):
        result += coef[i] * (x ** (len(coef)-i-1))

    return result


def interpol_lin(points,x):
    mn = points[0]
    mx = points[-1]

    for i in points:
        if (i[0] < x) and (i[0] > mn[0]):
            mn = i
        
        if (i[0] > x) and (i[0] < mx[0]):
            mx = i

    ds = (mx[1] - mn[1])/(mx[0] - mn[0])
    result = ((x - mn[0])*ds)+mn[1]

    return result


# Interpolacao de Monomios
def interpol_mon(points,value):
    n = len(points)
    v = np.zeros((n,n))
    const = np.zeros(n)

    for i in range(n):
        x,y = points[i]
        const[i] = y

        for j in range(n):
            v[i][j] = x ** j

    coef = np.linalg.solve(v,const)
    result = 0

    for i in range(len(coef)):
        result += coef[i] * (value ** i)

    return coef,result


# Interpolacao de Lagrange (original)
def interpol_lag(x,y):
  n = len(x)  
  maskb = np.arange(1, n + 1)  
  p = np.zeros_like(x, dtype=float)  
  L = np.zeros((n, n), dtype=float)  

  for jj in range(n):
    maskb[jj] = 0  
    mask = np.nonzero(maskb)[0]  
    maskb[jj] = jj + 1  
    den = 1  

    for ii in range(n):
      if ii != jj:
        den *= (x[jj] - x[ii])

    print("Denominador = ",den)
    coef = np.poly(x[mask]) 
    coef = (1 / den) * coef  
    L[jj, :] = coef  
    p += y[jj] * coef  

  return p, L  


# Interpolacao de Newton (original)
def interpol_new(x,y):
    sx = len(x)
    coef = np.zeros(sx)
    N = np.zeros((sx, sx))
    N[0, -1] = 1
    coef[0] = y[0]
    p = coef[0] * N[0, :]

    for jj in range(1, sx):
        num = 0
        for ii in range(jj):
            num += coef[ii] * np.polyval(N[ii, :], x[jj])
        N[jj, -jj - 1:] = np.poly(x[:jj])
        coef[jj] = (y[jj] - num) / np.polyval(N[jj, :], x[jj])
        p += coef[jj] * N[jj, :]

    return p, N, coef


# inicia os vetores
p = list(map(float,input().split()))
value = float(input())

M = mk_point(p)
x,y = mk_knots(p)


# Linear
print("\nLinear")
print("Resultado = ",interpol_lin(M,value))


# Monômio
M_coef,M_result = interpol_mon(M,value)
print("\n\nMonomial")
print("\nResultado = ",M_result)
print("Coeficientes = ", M_coef)


# Lagrange
print("\n\nLagrange\n")
pl, ll = interpol_lag(x,y)
print("\nResultado = ", interpol_value(pl,value))
print("Coeficientes de Lagrange = ",pl)
print("Matriz Lag = \n",ll)

# Newton
pn, pm, pc = interpol_new(x,y)
print("\n\nNewton")
print("\nResultado = ", interpol_value(pn,value))
print("Coeficientes = ", pc)
print("Matriz Newton = \n",pm)





"""
    O algorimo de newton pode ser otimizado construindo somente a diagona principal
    Para losta de nós muito grande seria uma economia de recursos
"""