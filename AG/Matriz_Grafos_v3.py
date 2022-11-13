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
        print("\n"
            "0 - Manual                     \n"
            "1 - Grafo completo             \n"
            "2 - Grafo Bipartido Completo   \n"
            "3 - Estrela                    \n"
            "4 - Caminho                    \n"
            "5 - Ciclo                      \n"
            "6 - Roda                       \n"
            "7 - Cubo                       \n")
        cmd2 = int(input("--> "))
        
        if cmd2 == 0:
            #Manual
            print()
            n = int(input("Insira o número de vértices: "))
            e = int(input("Insira o número de arestas: "))
           
            if (n>=0) and (e>=0):
                Mat_Adj = fill(n,e)
                save(n,e,Mat_Adj)

            else:
                print("\nO número de vértices e de arestas deve ser positivo!\n")

        elif cmd2 == 1:
            #Completo
            print()
            n = int(input("Insira o número de vértices: "))
            e = (n*(n-1))//2
            
            if (n>0) and (e>=0):
                Mat_Adj = mat(n)
                for i in range(n):
                    for j in range(i+1,n):
                        Mat_Adj[i][j] = 1
                        Mat_Adj[j][i] = 1
                save(n,e,Mat_Adj)
            
            else:
                print("\nO número de vértices deve ser positivo!\n")
        
        elif cmd2 == 2:
            #bipartido completo
            print()
            m1 = int(input("Insira o número de vértices do primeiro conjunto: "))
            m2 = int(input("Insira o número de vértices do segundo conjunto: "))
            e  = m1 * m2
            
            if (m1 > 0) and (m2 > 0):
                Mat_Adj = mat(m1+m2)
                for i in range(m1):
                    for j in range(m1,m1+m2):
                        Mat_Adj[i][j] = 1
                        Mat_Adj[j][i] = 1
                save(m1+m2,e,Mat_Adj)
            
            else:
                print("\nO número de vértices das partes deve ser positivo!\n")
        
        elif cmd2 == 3:
            #estrela
            print()
            n = int(input("Insira o número de vértices: "))
            e = n-1
            a = int(input("Escolha um vértice de %d a %d para ser o nó: "%(1,n)))
            Mat_Adj = mat(n)
            for i in range(n):
                if i != (a-1):
                    Mat_Adj[a-1][i] = 1
                    Mat_Adj[i][a-1] = 1
            save(n,e,Mat_Adj)
        
        elif cmd2 == 4:
            #caminho
            print()
            n = int(input("Insira o número de vértices: "))
            e = n-1
            
            if (n > 0):
                Mat_Adj = mat(n)
                for i in range(n-1):
                    Mat_Adj[i][i+1] = 1
                    Mat_Adj[i+1][i] = 1
                save(n,e,Mat_Adj)

            else:
                print("\nO número de vértices deve ser maior que 1!")

        elif cmd2 == 5:
            #Ciclo
            print()
            n = int(input("Insira o número de vértices: "))
            
            if n>3:
                e = n
                Mat_Adj = mat(n)
                
                for i in range (n-1):
                    Mat_Adj[i][i+1] = 1
                    Mat_Adj[i+1][i] = 1
                Mat_Adj[n-1][0] = 1
                Mat_Adj[0][n-1] = 1
                
                save(n,e,Mat_Adj)
            
            else:
                print("\nO número de vértices deve ser maior que 2!\n")

        elif cmd2 == 6:
            #roda
            print()
            n = int(input("Insira o número de vértices: "))

            if (n > 3):
                e = 2 * (n-1)
                Mat_Adj = mat(n)
                a = int(input("Escolha um vértice de %d a %d para ser o centro: "%(1,n)))
                
                for i in range (n):
                    if i != a-1:
                        Mat_Adj[a-1][i] = 1
                        Mat_Adj[i][a-1] = 1
                    Mat_Adj[i][i-1] = 1
                    Mat_Adj[i-1][i] = 1
                Mat_Adj[n-1][0] = 1
                Mat_Adj[0][n-1] = 1
                
                Mat_Adj[a][a-2] = 1
                Mat_Adj[a-2][a] = 1
                        
            
            save(n,e,Mat_Adj)

        elif cmd2 == 7:
            #cubo
            pass
        
        else:
            print("\nComando inválido!\n")
        
    
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
