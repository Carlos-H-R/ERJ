def teste1(c,l,r1,r2):
    lado = min(c,l)
    raio = max(r1,r2)
    diametro = 2*raio

    if (lado <= diametro):
        return True
    
    else:
        return False

def teste2(c,l,r1,r2):
    cat1 = l - (r1 + r2)
    cat2 = c - (r1 + r2)
    hip = (cat1 ** 2) + (cat2 ** 2)
    
    raios = (r1+r2) ** 2

    if (raios <= hip):
        return True
    
    else:
        return False

t = int(input())

for i in range(t):
    C,L,R1,R2 = map(int,input().split())

    if (teste1(C,L,R1,R2) and teste2(C,L,R1,R2)):
        print("S")

    else:
        print("N")