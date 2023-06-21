def sp(N):
    k = (N//2) - 1
    return (((k+1) ** 2) // 4)

def si(N):
    k = (N//2) - 1
    return ((k+1) * k)


base = [0] * 1000001    
for j in range(4,1000001):
    if (j == 4):
        base[j] = 1

    # else:
    #     base[j] = base[j-1] + (((j-1) * (j-3)) // 4)

    elif (j % 2 == 0):
        base[j] = base[j-1] + sp(j)

    else: 
        base[j] = base[j-1] + si(j)

t = int(input())

for i in range(t):
    N = int(input())

    print(base[N])


# tempo de processamento e resposta estah ok
# calculo da base esta incorreto
# verificar calculo