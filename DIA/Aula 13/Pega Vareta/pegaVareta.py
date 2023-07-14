class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Vareta:
    def __init__(self, o:Ponto, e:Ponto):
        self.o = o
        self.e = e
    

def sentido(p0: Ponto, p1: Ponto, p2: Ponto):
    s = ((p1.x - p0.x) * (p2.y - p0.y)) - ((p2.x - p0.x) * (p1.y - p0.y))
    
    if (s > 0):
        return 1
    elif (s < 0):
        return -1
    else: 
        return 0


def intercepta(v1:Vareta, v2:Vareta):
    p1 = v1.o
    p2 = v1.e
    p3 = v2.o
    p4 = v2.e
    return True

    # return ((max(p1.x,p2.x) >= min(p3.x,p4.x)) and
    #         (max(p3.x,p4.x) >= min(p1.x,p2.x)) and
    #         (max(p1.y,p2.y) >= min(p3.y,p4.y)) and
    #         (max(p3.y,p4.y) >= min (p1.y,p2.y))and
    #         (sentido(p1,p2,p3) * sentido(p1,p2,p4) <= 0) and
    #         (sentido(p3,p4,p1) * sentido(p3,p4,p2) <= 0))
    


t = int(input())

for i in range(t):
    N = int(input())
    J = [0]*N
    A = [0]*N

    coordJ = input().split()
    coordA = input().split()

    count_joao = 0
    count_advr = 0

    for j in range(N):
        k = 4*j
        J[j] = Vareta(Ponto(int(coordJ[k]),int(coordJ[k+1])),Ponto(int(coordJ[k+2]),int(coordJ[k+3])))
        A[j] = Vareta(Ponto(int(coordA[k]),int(coordA[k+1])),Ponto(int(coordA[k+2]),int(coordA[k+3])))

    for a in range(N):
        for b in range(a+1,N):
            if intercepta(J[a],J[b]): 
                count_joao += 1

            if intercepta(A[a], A[b]): 
                count_advr += 1
    
    if (count_joao > count_advr):
        print('+')
    
    elif (count_joao < count_advr):
        print('-')

    else:
        print('x')
    # o venecedor é aquele que deixo na mesa o maior numero de varetas cruzando     
