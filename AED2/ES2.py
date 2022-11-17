def matriz_torneio_v2(n):
    if n == 1:
        mat[1][1] = 1

    else:
        o = n//2
        matriz_torneio_v2(o)
        for i in range(1,o+1):
            for j in range(1,o+1):
                mat[i+o][j] = mat[i][j] + o
                k = n-(j-i+n)%o
                mat[i][j+o] = k
                mat[k][j+o] = i



n = int(input("Insira o número de times: "))
mat = []

for i in range(n+1):
    mat.append([0]*(n+1))

matriz_torneio_v2(n)

for i in range(1,n+1):
    print(*mat[i][1:n+1])
