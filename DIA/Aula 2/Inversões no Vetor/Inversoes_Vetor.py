def mergeSort(lista,count):

    if len(lista) > 1:

        meio = len(lista)//2
        #também é valido: meio = int(len(lista)/2)

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        count = mergeSort(listaDaEsquerda,count)
        count = mergeSort(listaDaDireita,count)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] <= listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
                count += len(listaDaEsquerda[i:])
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return count


t = int(input())

for i in range(t):
    vetor = list(map(int,input().split()))
    vetor = vetor[1:]
    count = 0

    print(mergeSort(vetor,count))
