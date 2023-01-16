from random import randint as rdit

def arranjo(conjunto, store, result):
    if (len(result) >= 100):
        return

    for i in conjunto:
        store.append(i)

        if (len(store) < 3):
            arranjo(conjunto,store,result)
            store.pop()

        else:
            result.append(store.copy())
            store.pop()


def combinacao(conjunto, store, result, n):
    if (len(store) == 4):
        result.append(store.copy())
        return
    
    for i in range(n,len(conjunto)):
        if (len(result) >= 100):
            return

        store.append(conjunto[i])
        combinacao(conjunto,store,result,i+1)
        store.pop()
    

elementos = [x for x in range(100)]

#Parte utilizada para gerar conjuntos aleatórios
# for i in range(3):
#     elementos.append(rdit(1,1000))

arr = []
com = []

arranjo(elementos,[],arr)
combinacao(elementos,[], com, 0)

print("Arranjo: ",*arr)
print("Combinação: ", *com)

# Neste código o arranjo foi configurado para selecionar subconjuntos de tamanho 3 e a combinação subconjuntos de tamanho 4.