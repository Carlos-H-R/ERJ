#Questão1_EC2_mod.py

#Questão 1

"""Falta implementar a versão para o Bottom-Up"""

def soma(vet):
    soma = 0
    for i in vet:
        soma += i
    return soma

#Utilizando o Top-Down
def subConTD(con, x):
    if x == 0:
        return True

    cop = con.copy()

    for i in cop:
        if i == x:
            return True

        elif i>x:
            cop.pop(cop.index(i))

    #pode implementar usando a recursão caso a soma seja menor que o parametro passado (sum < x)
    for i in range(len(cop)):
        cop2 = cop.copy()
        cop2.pop(i)
        sum = cop[i]
        
        for j in range(i,len(cop2)):
            if ((sum + cop2[j]) == x):
                return True

            elif ((sum + cop2[j]) < x):
                sum += cop2[j]

    return False
            

# Utilizando o Bottom-Up
def coisa(vet):
    k = 0
    memo = [-1]*(2**len(vet))
    memo[0] = 0

    for i in range(0,len(vet)):
        memo[k] = vet[i]
        k += 1

    print(*memo)

    for i in range(len(vet)):
        aux = vet[i]
        memo[k] = aux
        for j in range(i+1,len(vet)):
            k += 1
            aux += vet[j]
            memo[k] = (aux)

    return memo

            


def subConjBU(con):
    print(con)

    part = coisa(con)

    print(part)



def extra(vet):
    part = []

    for i in range(len(vet)):
        part.append()

    


key = True
while key:
    print("\n1 - cria/atualiza conjunto     "
          "\n2 - consulta com Top-Down      "
          "\n3 - consulta com Bottom-Up     "
          "\n4 - metodu extra               "
          "\n0 - encerra o programa       \n")

    key = int(input("--> "))

    if (key == 0):
        print("\nPrograma Encerrado!\n")
        key = False


    elif (key == 1):
        print("\nInsira o conjunto separando elementos com espaço\n")
        conjunto = list(map(int,input("--> ").split()))

        if (len(conjunto)>20):
            print("\nConjunto com mais elementos que o permitido!\n")
            del(conjunto)

    
    elif (key == 2):
        try:
            a = int(input("\nInsira o valor da soma buscada: "))
            
            if subConTD(conjunto,a):
                print("\nExiste subconjunto cuja soma é %d \n"%a)

            else:
                print("\nNão há subconjunto com essa soma\n")

        except ValueError:
            print("\nO valor da soma deve ser um número inteiro!\n")

        except NameError:
            print("\nNenhum conjunto foi criado!\n")

    
    elif (key == 3):
        subConjBU(conjunto)

    elif (key == 4):
        result = []

        for i in range(len(conjunto)):
            result.append(extra(conjunto, 0))

        print(result)
    
    else:
        print("\nEntrada Inválida!\n")