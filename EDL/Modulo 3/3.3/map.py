def map_f(funcao,lista):
    for i in range(len(lista)):
        lista[i] = funcao(lista[i])
    return id(lista)

# exemplo
a = [1,2,3,4,5,6]

f = lambda x : (2*x)

print(a)
print(map_f(f,a))
print(a)