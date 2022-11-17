def matriz_torneio(n):
    if n == 2:
        mat[1][1] = 1
        mat[1][2] = 2
        mat[2][1] = 2
        mat[2][2] = 1

    elif (n%2) != 0:
        matriz_torneio(n+1)
        limpa()

    else:
        o = n//2
        matriz_torneio()
        
        if (o%2) == 0:
            pass

        else:
            pass


n = int(input("Insira o número de times: "))
mat = []

for i in range(n+1):
    mat.append([0]*(n+1))

matriz_torneio(n)

for i in range(1,n+1):
    print(mat[i][1:n+1])
