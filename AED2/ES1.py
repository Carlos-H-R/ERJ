import random

def meio(a,b):
    return (a+b)//2

def part(Vet):
    if len(Vet)>1:
        pivot = len(Vet)

        smaller = []
        bigger = []

        for i in Vet:
            if i <= Vet[pivot]:
                smaller.append(i)
            else:
                bigger.append(i)

        return (part(smaller)+Vet[pivot]+part(bigger))

    else:
        return Vet

def cria():
    tamanho = input("Tamanho do vetor: ")
    i, f = map(int,input("Menor e maior valor do vetor: ").split())
    # for i in range(i,f+1):




def Bin_Search(Vet, i, f, key):
    if Vet[i] <= key <= Vet[f]:

        m1 = meio(i,meio(i,f))
        m2 = meio(meio(i,f),f)

        if key == Vet[m1]:
            return Vet[m1]

        elif key == Vet[m2]:
            return Vet[m2]

        elif key < Vet[m1]:
            return Bin_Search(Vet, i, m1-1, key)

        elif Vet[m1] < key < Vet[m2]:
            return Bin_Search(Vet, m1+1, m2-1, key)

        else:
            return Bin_Search(Vet, m2+1, f, key)

    else:
        return -1

chave = int(input("Insira o numero procurado: "))
memo = [1,6,9,11,16,21,26,30,37,45,55,62,69,73,74]

result = Bin_Search(memo,0,len(memo)-1,chave)
print(result)

while True:
    print("A -> para criar novo vetor \n"
    "B -> para buscar no vetor \n"
    "C -> para encerrar \n")
    cmd = input("Insira o comando -> ")

    if cmd.lower() == 'a':
        ss

    elif cmd.lower() == 'b':
        ss

    elif cmd.lower() == 'c':
        print("\nPrograma encerrado!!! \n")
        break

    else:
        print("\n\nComando Inválido!!!\n\n")