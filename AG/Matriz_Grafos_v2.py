import json

def mat(size):
    v = []
    for i in range(size):
        aux = [0]*size
        v.append(aux)
    return v

def fill(n,e):
    vet = mat(n)
    print("\nOs vertices estão conectados?  "
          "\n1 - para SIM/ 0 - para NÃO)\n")
        
    for j in range(0,n):
        for i in range(j+1,n):
            aux = int(input("%d e %d: "%(i+1,j+1)))
            vet[i][j] = aux
            vet[j][i] = aux

            if aux == 1:
                e -= 1

            if e == 0:
                return vet

def save(v,a,mat):
    nome = str(input("\nNome do grafo: "))
    file.seek(0)
    dic = json.load(file)
    dic.update({nome: (v,a,mat)})
    file.seek(0)
    file.write(json.dumps(dic))
    file.truncate()


file = open('Grafos.json',"r+")

if not file.readline():
    file.write('{}')

while not file.closed:
    print()
    print("Comando A - para ler novo grafo\n"
          "Comando B - para buscar grafo pelo nome\n"
          "Comando X - para encerrar o programa\n")
    cmd = input("Insira o comando: ")
    
    if cmd.lower() == 'a':
        print()
        n = int(input("Insira o número de vértices: "))
        e = int(input("Insira o número de arestas: "))
        Mat_Adj = fill(n,e)
        save(n,e,Mat_Adj)
    
    elif cmd.lower() == 'b':
        key = str(input("\nInsira o nome do grafo: "))
        file.seek(0)
        dic = json.load(file)
        try:
            result = dic[key]
            print()
            for i in result[2]:
                print(*i)

        except:
            print("\n\nGrafo não encontrado!\n\n")

    elif cmd.lower() == 'x':
        print("\nPrograma encerrado!")
        file.close()

    else:
        print("\n\nComando Inválido!\n\n")
