a1 = int(input("Insira o primeiro termo da progressão: "))
r = int(input("\nInsira a razão da progressão: "))
n = int(input("\nQuantos termos devem ser exibidos: "))

pa = []
a = a1
for i in range(0,n):
    pa.append(a)
    a += r

print("")
print(pa)
