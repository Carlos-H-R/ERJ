# Cria o vetor que aloca os dados dos crivo
def GeraCrivo(n):
    sq = n ** (1/2)
    sq = int(sq) + 1
    print(sq)

    c = [1,1] + list(range(2,n+1))

    i=2
    while(i <= n):
        c[i] = 2
        i += 2

    i = 3
    while (i <= sq):
        if c[i] == i:
            t = i*i
            d = i+i
            
            while (t <= n):
                if (c[t] == t):
                    c[t] = i
                t += d
        i += 1
    return c

# Gera tabela de primos
def GeraTabPrimos (r,c):
    p = []

    for i in range(2,r+1):
        if (c[i] == i):
            p.append(i)

    return p


# execucao do problema

crivo = GeraCrivo(31700000)
primo = GeraTabPrimos(31700000,crivo)

t = int(input())

for i in range(t):
    n = int(input())

    if (primo[n] == n):
        print("N")

    else:
        print("S")
