# Algoritmo

def falseCount(vet):
    if len(vet) == 0:
        return 0

    elif len(vet) == 1:
        if vet[0].lower() == "v":
            return 0

        else:
            return 1
    
    else:
        n = (len(vet)-1)//2

        if vet[n].lower() == "v":
            return falseCount(vet[n+1:len(vet)])

        else:
            return (falseCount(vet[0:n]) + (len(vet)-(n)))



# Interface de teste

def tabela(n,m):
    return (verdadeiros+falsos)

verdadeiros = ['v'] * int(input("Número de itens verdadeiros: "))
falsos = ['f'] * int(input("\nNúmero de itens falsos: "))
vetor = verdadeiros+falsos

print("\n",vetor,"\n")

a = falseCount(vetor)
print("\nNúmero de F's é %d"%a)