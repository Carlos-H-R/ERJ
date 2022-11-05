print("Insira numeros inteiros \nPara encerrar a lista digite 0 \n")
par = []
imp = []

lock = True
while lock:
    n = input("--> ")
    if n.isdigit():
        n = float(n)
        if n%1 == 0:
            n = int(n)
            if n == 0:
                lock = False
            elif n % 2 == 0:
                par.append(n)
            else:
                imp.append(n)
        else:
            print("Entrada Inválida! \nDigite um número inteiro! \n")
    else:
            print("Entrada Inválida! \nDigite um número inteiro! \n")

med = 0
for i in range(0,len(par)):
    med += par[i]
    
print("Há %i números pares e %i números ímpares"%(len(par),len(imp)))
print("\nA média dos números pares é %.1f"%(med/len(par)))
        
