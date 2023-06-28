from math import sqrt

class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def distPonto(A:Ponto,B:Ponto):
    dx = A.x - B.x
    dy = A.y - B.y

    dr2 = (dx ** 2) + (dy ** 2)

    return sqrt(dr2)


t = int(input())

for i in range(t):
    plano = []
    NR, NA, NO = 0, 0 ,0

    N = int(input())
    
    coor = list(map(int,input().split()))

    for j in range(0,2*N,2):
        a = coor[j]
        b = coor[j+1]
        plano.append(Ponto(a,b))
        
    for k in range((2*N)-2):
        for h in range(k+1,2*N):
            for g in range(j+1,2*N):
                l1 = distPonto(plano[k],plano[h])
                l2 = distPonto(plano[k],plano[g])
                l3 = distPonto(plano[h],plano[g])

                c = max(l1, l2, l3)
                max
