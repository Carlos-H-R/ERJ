print("CATÁLOGO DE PRODUTOS \n")

nome = []
price = []

lock = True
while lock:
    n = input("\nInsira o nome do produto: ")
    if n == 'xxx' or n == 'XXX':
        lock = False
    else:
        nome.append(n)
        
        a = True
        while a:
            p = input("Insira o preço do produto: ")

            if p.isdigit():
                p = float(p)
                test = price.count(p)
                if test == 0:
                    price.append(p)
                    a = False
                else:
                    print("Preço já registrado!\n")
            else:
                print("\nDeve ser preenchido dígitos!\n")


most = 0
for i in range(0,len(price)):
    if price[i] > most:
        most = price[i]
        prod = nome[i]

print("O produto mais caro é %s custndo R$%.0f"%(prod,most))
