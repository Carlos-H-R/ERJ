def fltr(function,lista):
    result = []
    
    for i in lista:
        if (function(i)):
            result.append(i)

    return result


# Exemplo
l = [1,2,3,4,5,6]

def impar(a):
    if (a%2) == 0:
        return False
    else:
        return True

print(fltr(impar,l))
# Resultado = [1,3,5]