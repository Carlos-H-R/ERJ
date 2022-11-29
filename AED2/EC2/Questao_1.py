#Questão 1

"""Falta implementar a versão para o Bottom-Up"""

# def soma(vet):
#     soma = 0
#     for i in vet:
#         soma += i
#     return soma

#Utilizando o Top-Down
def subConTD(con, x):
    if x == 0:
        return True

    cop = con.copy()

    for i in cop:
        if i == x:
            return True

    for i in cop:
        if i>x:
            cop.pop(cop.index(i))

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
            
"""
#Utilizando o Bottom-Up
def coisa(vet, x):
    if x == 0:
        vet.append([])
        return vet

    else:
        for i in x:
            aux = []
            cop = vet.copy()

            


def subConjBU(con, x):
    sum = 0
    part = []
    
    part = coisa(part)

    print(part)
"""

key = True
while key:
    print("\n1 - cria/atualiza conjunto     "
          "\n2 - consulta com Top-Down      "
          "\n3 - consulta com Bottom-Up     "
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
        print("\nNão implementada ainda!\n")

    
    else:
        print("\nEntrada Inválida!\n")