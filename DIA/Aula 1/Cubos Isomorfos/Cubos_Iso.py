eixo1 = [1,2,4,3]
eixo2 = [0,3,5,2]
eixo3 = [0,4,5,1]

def rot(cubo, eixo):
    aux = cubo[eixo[0]]
    for i in range(3):
        cubo2[eixo[i]] = cubo2[eixo[i+1]]
    
    cubo2[eixo[3]] = aux

def testa(cubo_base, cubo_rot):
    if (cubo_base == cubo_rot):
        return 1
    
    else:
        return 0


t = int(input())

for m in range(t):
    cubo1 = list(input())
    cubo2 = list(input())

    test = 0
    test += testa(cubo1,cubo2)

    for i in range(4):
        rot(cubo2,eixo1)
        test += testa(cubo1,cubo2)

        for j in range(4):
            rot(cubo2, eixo2)
            test += testa(cubo1,cubo2)

            for k in range(4):
                rot(cubo2,eixo3)
                test += testa(cubo1,cubo2)


    if (test > 0):
        print("S")

    else:
        print("N")
