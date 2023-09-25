import numpy as np

def egm(A,b,m,n):
    aux=[]
    Ab = A
    bb = b

    for i in range(n):
        id_aux = np.identity(m)
        for j in range(i+1,m):
            id_aux[j,i] = -Ab[j,i]/Ab[i,i]
        Ab = id_aux@Ab
        bb = id_aux@bb
        
        aux.append(id_aux)
    return np.triu(Ab),bb,aux

def mult(X):
    x = 1
    for i in X:
        for j in i:
            x *= j
    return x

def e_gauss(A,b, m, n):
    mb = 1
    nb = n
    Ab = np.block([A,b])
    for i in range(1,m):
        for j in range(i,m):
            line_multi = Ab[j,i-1]/Ab[i-1,i-1]
            for k in range(0,m+1):
                Ab[j,k] = Ab[j,k] - line_multi*Ab[i-1,k]
    T = np.triu(Ab[:,0:n])
    y = Ab[:,n:n+1]
    return T,y

A = []
m,n = map(int, input().split())
for i in range(m):
    A.append(list(map(float,input().split())))
A = np.array(A)

auxb = list(map(float,input().split()))
b = []
for i in auxb:
    b.append([i])
b = np.array(b)




print(A)
print(b)
# [U, bu] = e_gauss(A,b,m,n)
[U,bu,aux] = egm(A,b,m,n)
print('U =\n',U)
print('bu=\n',bu)
Y = np.linalg.solve(U,bu)
print('Soma Y = ', sum(Y))
print('Prod Y = ', mult(Y))

for i in range(len(aux)):
    print('A%d =\n'%(i+1),aux[i])