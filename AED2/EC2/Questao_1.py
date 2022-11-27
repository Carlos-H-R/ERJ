#Questão 1

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
            

#Utilizando o Bottom-Up
def subConjBU(con, x):
    sum = 0
    part = [[]]
    
    for i in con:
        pass

    print(part)


key = True
while key:
    print("\n1 - cria conjunto aleatório    "
          "\n2 - cria conjunto manualmente  "
          "\n3 - consulta com Top-Down      "
          "\n4 - consulta com Bottom-Up     "
          "\n0 - encerra o programa       \n")

    key = input("--> ")

    if (key == 0):
        print("\nPrograma Encerrado!\n")
        key = False

    elif (key == 1):
        pass

    elif (key == 2):
        pass

    elif (key == 3):
        pass

    elif (key == 4):
        pass

    else:
        print("\nEntrada Inválida!\n")