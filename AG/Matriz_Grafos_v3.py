def mat(size):
    v = []
    for i in range(size):
        aux = [0]*size
        v.append(aux)
    return v

def printMat(mat):
    aux = mat.split("_")
    for i in aux:
        i.removeprefix("[")
        i.removesuffix("]")
        i = i.split(", ")
        print(*i)

def convstr(mat):
    aux = ""
    for i in mat:
        aux += "_" + str(i)
    return aux

def fill(n):
    vet = mat(n)
    a = 0
    print("Os vertices estão conectados?  "
          "\n1 - para SIM/ 0 - para NÃO)\n")
    
    for i in range(0,n):
        for j in range(i,n):
            aux = int(input("V%d e V%d: "%(i,j)))
            vet[i][j] = aux
            vet[j][i] = aux
            if aux==1:
                a += 1
    
    return (vet,a)

lock = True
while lock:
    file = open('Grafos.txt',"a+")
    print("Comando A para ler novo grafo\n"
          "Comando B para buscar grafo pelo nome\n"
          "Comando C para encerrar o programa\n")
    cmd = input("Insira o comando: ")
    
    if cmd.lower() == 'a':
        grafo = ""
        grafo += str(input("\nNome do grafo: ")) + "/"
        n = int(input("Insira o número de vértices: "))
        Mat_Adj,e = fill(n)
        grafo += str(n) + "/" + str(e) + "/" + convstr(Mat_Adj) + "\n"
        file.write(grafo)
    
    elif cmd.lower() == 'b':
        a = True
        file.seek(0)
        key = str(input("\nInsira o nome do grafo: "))
        for line in file:
            data = list(line.split("/"))
            if key == str(data[0]):
                printMat(data[3])
                a = False
        
        if a:
            print("\n\nGrafo não encontrado!\n\n")
            


    elif cmd.lower() == 'c':
        print("\nPrograma encerrado!")
        file.close()
        lock = False
    
    else:
        print("\n\nComando Inválido!\n\n")

exit()

""" Para versão 4 podemos substituir o uso da matriz e usar um map e um struct para organizar os dados e acessar com facilidade
    Podemos melhorar a formatação do arquivo de texo para que fique mais legível mas isso requer alteração no módulo de leitura do arquivo"""