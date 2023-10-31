import numpy as np

def general(A,x,b,max=100,tol=1e-10):
    [m,n] = A.shape

    dA = np.diag(A).reshape(m,1)
    x0 = b/dA

    for i in range(max):
        r = b - A@x0
        xf = x0+r/dA
        
        EA = np.linalg.norm(x-x0)
        ER = EA/np.linalg.norm(x)

        if(ER <= tol):
            break
    
    return x


def jacobi(A,x,b,max,tol=1e-9):
    M = np.diag(np.diag(A))
    N = M - A

    for i in range(max):
        x1 = x.copy()
        x  = np.linalg.solve(M,(N@x+b))
        e  = np.linalg.norm(x - x1) / np.linalg.norm(x)

        if (e <= tol):
            break
    
    return x


def seidel(A,x,b,max,tol=1e-9):
    M = np.tril(A)
    N = M - A

    for i in range(max):
        x1 = x.copy()
        x  = np.linalg.solve(M,(N@x+b))
        e  = np.linalg.norm(x - x1) / np.linalg.norm(x)

        if (e <= tol):
            break
    
    return x


# Define a dimencao da matriz lida
m,n,iter = map(int, input().split())

# Lê uma matriz a e armazena A
A  = []
for i in range(m):
    A.append(list(map(float,input().split())))
A = np.array(A)

# Lê o vetor solucao
auxb = list(map(float,input().split()))
b = []
for i in auxb:
    b.append([i])
b = np.array(b)

# Lê o vetor X
auxb = list(map(float,input().split()))
x = []
for i in auxb:
    x.append([i])
x = np.array(x)


# Operacoes

R = jacobi(A,x,b,iter)
# R = seidel(A,x,b,iter)
# R = general(A,x,b,iter)

np.set_printoptions(precision=4,suppress=True)
print("x =\n",R)
