import random

def meio(a,b):
    return (a+b)//2

def QuickSort(Vet, i, f):
    if i < f:
        pivot = Vet[i]
        aux = i

        for j in range(i+1,f+1):
            if Vet[j] <= pivot:
                aux += 1
                Vet[j], Vet[aux] = Vet[aux], Vet[j]
        
        Vet[i], Vet[aux] = Vet[aux], Vet[i]

        QuickSort(Vet, i, aux-1)
        QuickSort(Vet, aux+1, f)
        
        return Vet

    else:
        return Vet

def cria():
    vetor = []
    tamanho = int(input("Tamanho do vetor: "))
    i, f = map(int,input("Menor e maior valor do vetor: ").split())
    
    for i in range(tamanho):
        vetor.append(random.randint(i,f))
    
    return vetor


def Bin_Search(Vet, i, f, key):
    if Vet[i] <= key <= Vet[f]:

        m1 = meio(i,meio(i,f))
        m2 = meio(meio(i,f),f)

        if key == Vet[m1]:
            return m1

        elif key == Vet[m2]:
            return m2

        elif key < Vet[m1]:
            return Bin_Search(Vet, i, m1-1, key)

        elif Vet[m1] < key < Vet[m2]:
            return Bin_Search(Vet, m1+1, m2-1, key)

        else:
            return Bin_Search(Vet, m2+1, f, key)

    else:
        return -1

memo = []

while True:
    print("\n\n"
    "A -> para criar vetor aleatório\n"
    "B -> para cria vetor personalizado\n"
    "C -> para visualizar o vetor atual\n"
    "D -> para buscar no vetor \n"
    "X -> para encerrar \n")
    cmd = input("Insira o comando -> ")

    if cmd.lower() == 'a':
        memo = cria()
        memo = QuickSort(memo,0,len(memo)-1)

    elif cmd.lower() == 'b':
        print("\nInsira os valores do vetor separados por espaço")
        memo = list(map(int,input("-> ").split()))
        memo = QuickSort(memo,0,len(memo)-1)

    elif cmd.lower() == 'c':
        if len(memo) != 0:
            print(*memo)
        
        else:
            print("\nVetor Vazio!\n")

    elif cmd.lower() == 'd':
        if len(memo) != 0:
            chave = int(input("Insira o numero procurado: "))
            result = Bin_Search(memo,0,len(memo)-1,chave)

            if result != -1:
                print("O valor buscado está na posição %d"%result)

            else:
                print("\nValor não encontrado!\n")
        
        else:
            print("\nVetor Vazio!\n")
    
    elif cmd.lower() == 'x':
        print("\nPrograma encerrado!!! \n")
        break

    else:
        print("\n\nComando Inválido!!!\n\n")