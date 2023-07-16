t = int(input())

for i in range(t):
    # n = quantidade de estacoes de metro com elevador
    # d = quantidade de possiveis locais turisticos
    n,d = map(int,input().split())

    # lista com posicoes de cada estacao com elevador
    A = list(map(int,input().split()))

    # lista com posicoes das estacoes com ponto turistico
    D = list(map(int,input().split()))

    # lista com as estacoes com elevador mais proximas de P.Turistico
    P = []

    for j in D:
        min_dist = [A[0],abs(j-A[0])]

        for k in range(1,n):
            if (abs(j-A[k]) < min_dist[1]):
                min_dist = [A[k],abs(j-A[k])]
            
            elif (abs(j-A[k]) == min_dist[1]):
                if (A[k] < min_dist[0]):
                    min_dist = [A[k],abs(j-A[k])]

        P.append(min_dist[0])

    print(*P)
