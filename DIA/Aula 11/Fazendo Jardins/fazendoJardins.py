from math import sqrt
from math import pi

def area_triangulo(s,l1,l2,l3):
    return sqrt(s * (s-l1) * (s-l2) * (s-l3))

def area_circulo(raio):
    return (pi * raio * raio)


t = int(input())

for i in range(t):
    a,b,c = map(int,input().split())

    s = (a + b + c) / 2
    A = area_triangulo(s,a,b,c)

    r = A/s
    R = (a * b * c) / (4 * A)

    vermelha = area_circulo(r)
    violeta = A - vermelha
    amarela = area_circulo(R) - A

    print("%.2f %.2f %.2f"%(amarela,violeta,vermelha))