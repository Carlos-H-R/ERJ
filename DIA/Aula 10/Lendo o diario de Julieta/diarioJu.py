def verifica(frase,palavra):
    f = len(frase)
    p = len(palavra)
    for i in range(f - p + 1):
        if (frase[i] == palavra[0]):
            aux = frase[i:(p+i)]
            if (aux == palavra):
                return True
    return False

def decript(frase,chave):
    desencriptado = []
    for i in frase:
        idx = (i+chave) % 26
        desencriptado.append(idx)
    
    return desencriptado


def testChave(frase,palavra):
    for j in range(1,27):
        aux = decript(frase,j)
        if (verifica(aux,palavra)):
            trad = list(map(lambda x : chr(x+96),aux))
            trad = "".join(trad)
            return trad

t = int(input())

for i in range(t):
    frase = list(map((lambda x : ord(x)-96),list(input())))

    palavra = list(map((lambda x : ord(x)-96),list(input())))

    print(testChave(frase,palavra))
