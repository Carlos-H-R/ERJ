#Questão 2

#ALgoritmo apenas verifica se a mensagem foi excrita por Alice ou pelo irmão
#As mensagens e resultados não são guardados

def verify(i, sample, padrao):
    check = 0
    first = padrao[0]
    sampleCopy = list(sample)

    for j in sampleCopy:
        if (j == first):
            m = sampleCopy.index(j)
            n = m + len(padrao)
            
            if (''.join(sampleCopy[m:n]) == padrao):
                check += 1
                sampleCopy = sampleCopy[n:].copy()

    if (check == i):
        return True

    else:
        return False


key = True
while key:
    print("\n1 - Checar mensagem"
          "\n0 - Encerra")

    try:
        key = int(input("--> "))

        if (key ==  1):
            try:
                i = int(input("\nInsira o número de vezes que o padrão deve ocorrer: "))
                p = input("Insira o padrão: ")
                mensagem = input("Insira a mensagem: ")

                if verify(i,mensagem,p):
                    print("\nMensagem enviada pela Alice.\n")

                else:
                    print("\nMensagem enviada pelo irmão da Alice. \n")

            except NameError or ValueError:
                print("\nO campo número de vezes deve conter um número inteiro!\n")

        elif (key == 0):
            print("\nEncerrado!\n")

        else:
            print("\nComando Inválido!\n")

    except:
        print("\nComando Inválido!\n")