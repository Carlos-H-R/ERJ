def mod1(vet,i,f):
    if i < f:
        pivot = vet[i]
        aux = i

        for j in range(i+1,f+1):
            if vet[j] == pivot:
                aux += 1
                vet[j], vet[aux] = vet[aux], vet[j]
        
        vet[i], vet[aux] = vet[aux], vet[i]

        mod1(vet, i, aux-1)
        mod1(vet, aux+1, f)
        
        return vet

    else:
        return vet

print("Para testar insira o elementos separados por espaço e garanta" 
      "que um dos elementos atenda a condição para ser maioria\n    ")

array = input("Insira o elementos separados por espaço:\n-->  ").split()

ordenado = mod1(array,0,len(array)-1)

print("O elemento que representa a maioria é: ",ordenado[(len(ordenado)-1)//2])