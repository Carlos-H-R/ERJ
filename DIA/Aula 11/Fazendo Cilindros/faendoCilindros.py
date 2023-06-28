from math import pi

def volCilinder(raio, altura):
    base = pi * raio * raio
    return (base * altura)

def fazCilinder(c,l):
    r1 = (c/(2*pi))
    a1 = (l-r1)
    V1 = volCilinder(r1,a1)

    x = l / (2 * (pi + 1))
    r2 = min((c/2),x)
    a2 = c
    V2 = volCilinder(r2,a2)

    if V1>V2:
        return V1
    
    else:
        return V2

t = int(input())

for i in range(t):
    C, L = map(int,input().split())
    
    if C < L:
        result = (fazCilinder(C,L))

    else:
        result = fazCilinder(L,C)

    print("%.2f"%result)
