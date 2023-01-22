from random import randint as rdi

def distribuiAntena(x,raio):
    a = [x[0]+raio]
    for i in range(1,len(x)):
        if (x[i] > (a[len(a)-1]+raio)):
            a.append(x[i]+raio)
    
    return a

#Gerador aleatório de valores para testar o algoritmo
raio = rdi(1,15)
casas = []
for i in range(20):
    casas.append(rdi(0,100))

#Ordena o vetor com as posições das casas
casas.sort()
print(raio)
print(casas)


antenas = distribuiAntena(casas,raio)
print(antenas)
print(len(antenas))
