def mtx3():
    vet = []
    for i in range(3):
        vet.append(list(map(int,input(f"Linha {i+1}: ").split(','))))
    return vet

def det(m):
    pri = 0
    sec = 0
    for i in range(3):
        pri += (m[0][i-3]*m[1][i-2]*m[2][i-1])
    for i in range(-2,1):
        sec += (m[0][i+2]*m[1][i+1]*m[2][i])
    det = pri - sec
    return det

print("Para criar uma matriz\ndigite cada lilha com \nelemntos separados por vírgula\n")
d = det(mtx3())
print(f"O determinante da matriz inserida é {d}")
