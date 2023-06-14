# confere se a palavra está na frase
def verifica(frase,palavra):
    f = len(frase)
    p = len(palavra)
    for i in range(f - p + 1):
        if (frase[i] == palavra[0]):
            aux = frase[i:(p+i)]
            if (aux == palavra):
                return True
    return False

# aplica a chave na frase
def decript(frase,chave):
    desencriptado = ""
    for i in frase:
        x = ord(i) + chave

        if x > 122:
            x -= 26

        desencriptado += chr(x)
    
    return desencriptado

# realiza o teste com todas as chaves
def testChave(frase,palavra):
    for j in range(1,27):
        aux = decript(frase,j)
        if (verifica(aux,palavra)):
            return aux

t = int(input())

for i in range(t):
    frase = str(input())

    palavra = str(input())

    print(testChave(frase,palavra))
