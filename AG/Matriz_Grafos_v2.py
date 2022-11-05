def mat(size):
    v = []
    for i in range(size):
        aux = [0]*size
        v.append(aux)
    return v

def printMat(mat,k):
    for i in range(k):
        print(mat[i])
            

def fill(n):
    vet = mat(n)
    a = 0
    print(vet,n)
    print("Os vertices estão conectados?  "
          "\n1 - para SIM/ 0 - para NÃO)\n")
    
    for i in range(0,n):
        for j in range(i,n):
            aux = int(input("%d e %d: "%(i+1,j+1)))
            vet[i][j] = aux
            vet[j][i] = aux
            if aux==1:
                a += 1
    
    return (vet,a)

lock = True
Grafos = []

while lock:
    file = open('Grafos.txt',"a+")
    print("Comando A para ler novo grafo\n"
          "Comando B para buscar grafo pelo nome\n")
    cmd = input("Insira o comando: ")
    
    if cmd.lower() == 'a':
        nome = str(input("\nNome do grafo: "))
        n = int(input("Insira o número de vértices: "))
        Mat_Adj,e = fill(n)
        grafo = [nome,n.e,Mat_Adj]
        Grafos.append(grafo)
    
    elif cmd.lower() == 'b':
        a = False
        key = str(input("\nInsira o nome do grafo: "))
        for grafo in Grafos:
            if key == str(grafo[0]):
                printMat(graf[3],int(graf[1]))
                a = True
        if a:
            break
        print("\n\nGrafo não encontrado!\n\n")

    elif cmd.lower() == 'c':
        print("\nPrograma encerrado!")
        #file.close()
        lock = False
    
    else:
        print("\n\nComando Inválido!\n\n")
