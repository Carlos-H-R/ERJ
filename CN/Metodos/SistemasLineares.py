import numpy as np


def cramer(A, b, min=1e-15):
    dim = A.shape

    if (dim[0] != dim[1]):
        print('A matriz deve ser quadrada!')
        x = np.NAN
        status = 1
        return x,status
    
    dimb = b.shape
    if (dim[0] != dimb[0]):
        print('A matriz e o vetor devem ter o mesmo numero de linhas!')
        x = np.NAN
        status = 2
        return x,status
    
    detA = np.linalg.det(A)
    if (abs(detA) < min):
        print('Determinante da matriz inferior ao minimo!')
        x = np.NAN
        status = 3
        return x,status
    
    if (np.isinf(abs(detA))):
        print('Determinante infinito!')
        x = np.NAN
        status = 4
        return x,status
    
    x = np.zeros((dim[1],1))
    for i in range(dim[0]):
        aux = A[:,i:i+1].copy()
        A[:,i:i+1] = b.copy()
        x[i] = np.linalg.det(A)/detA
        A[:,i:i+1] = aux.copy()
    status = 0
    return x,status


c1 = list(map(float, input().split()))
c2 = list(map(float, input().split()))
c3 = list(map(float, input().split()))
cb = list(map(float, input().split()))

cbb = []
for i in cb:
    cbb.append([i])

A = np.array([c1,c2,c3])
b = np.array(cbb)


mindet=1e-10
saida =cramer(A,b,mindet)
print(saida[0])


# if saida[1]==0:
#   x=np.linalg.solve(a,b)
#   print(x)
#   print(saida[0])
#   normerro = np.linalg.norm(x-saida[0])/np.linalg.norm(x)
#   print('norma do erro = {:+.6e}.'.format(normerro))

"""
import numpy as np

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))
lb = list(map(int, input().split()))

a = np.block([np.array(l1)],[np.array(l2)],[np.array(l3)])
b = np.block([np.array(lb)])

s = np.linalg.solve(a,b)
print(x)
"""