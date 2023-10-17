import numpy as np

def fact_LU(A):
    n,m = A.shape

    for i in range(m-1):
        for j in range(i+1,m):
            A[j,i] = A[j,i] / A[i,i]

            for k in range(i+1,m):
                A[j,k] = A[j,k] - A[j,i]*A[i,k]

    U = np.triu(A)
    L = np.tril(A,-1) + np.identity(m)
    return L,U

# Define a dimencao da matriz lida
m,n = map(int, input().split())

# #Lê uma matriz a e armazena A
# A  = []
# for i in range(m):
#     A.append(list(map(float,input().split())))
# A = np.array(A)

# Lê o vetor solucao
auxb = list(map(float,input().split()))
b = []
for i in auxb:
    b.append([i])
b = np.array(b)


# Lê a matriz LU e separa em Upper e Lower
LU = []
for i in range(m):
    LU.append(list(map(float,input().split())))
LU = np.array(LU)

L = np.tril(LU,-1)+np.identity(m)
U = np.triu(LU)



# print("\nA =\n",A)
# # print(b)

# Extrai a Lower e a Upper a partir da matriz A
# [L,U] = fact_LU(A)

print("\nU =\n",U)
print("\nL =\n",L)
print("\nA =\n",L@U)
print("\nAb =\n",np.block([L@U,b]))

print("det A = ",np.linalg.det(L@U))
print("det L = ",np.linalg.det(L))
print("det U = ",np.linalg.det(U))
