def mat(size):
    v = []
    for i in range(size):
        aux = [0]*size
        v.append(aux)
    return v

def printMat(mat,k):
    for i in range(k):
        print(*mat[i])
            

def fill(n):
    vet = mat(n)
    a = 0
    print(vet,n)
    print("Os vertices estão conectados?  "
          "\n1 - para SIM/ 0 - para NÃO)\n")
    for i in range(0,n):
        for j in range(0,n):
            aux = int(input("%d e %d: "%(i+1,j+1)))
            vet[i][j] = aux
            if aux==1:
                a += 1
    return (vet,a)

n = int(input("Insira o número de vértices: "))
Mat_Adj,e = fill(n)
print("\n")
printMat(Mat_Adj,n)
