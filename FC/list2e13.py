def createM(m,n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):            
            mat[i].append(float(input()))
    return(mat)

def somaM(mat1,mat2):
    if len(mat1[0]) == len(mat2):
        matS = []
        for i in mat1:
            matS.append([])
            for j in range(len(mat2[0])):
                e = 0
                for k in range(len(mat2)):
                    e += i[k]*mat2[k][j]
                matS[mat1.index(i)].append(e)
        return(matS)
    else:
        print('Erro! Soma não realizada!')
        return ([])

def Mtrans(mat):
    mt = []
    for i in range(len(mat[0])):
        mt.append([])
        for j in range(len(mat)):
            mt[i].append(mat[j][i])
            print(mt)
    return(mt)
