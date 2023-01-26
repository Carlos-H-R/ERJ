#Função que executa o algoritmo aplicando o método guloso
def menorNum(n,c):
    counter = 0
    
    for i in c:
        while (n >= i):
            n -= i
            counter += 1

    if (n == 0):
        return counter

    else:
        return (counter + 1)



w = int(input("Número de comprimidos: "))
p = list(map(int,input("Capacidade de cada frasco separado por espaço: \n").split()))

#Ordena o vetor com as capacidades dos frascos em ordem decrescente
p.sort(reverse=True)
print("\nO menor número de frascos é: %d"%menorNum(w,p))

"""
Este algoritmo retorna o menor número de frascos contanto que o conjunto
 que representa as capacidades dos frascos seja um conjunto guloso.
"""

