nome = []
idade = []
sexo = []
salario = []

print("COLETA DE DADOS \n Para encerrar digite 0 no campo idade \n")

lock = True
while lock == True:
    print("")
    nome.append(input("Insira o nome do funcionário: "))

    a = True
    while a:
        age = input("Insira a idade: ")
        if age.isdigit():
            idade.append(int(age))
            a = False
        else:
            print("Entrada Inválida!")

    b = True
    while b:
        sex = input("Selecione o sexo do funcionário (M/F): ")
        if sex == 'M':
            sexo.append('M')
            b = False
        elif sex == 'F':
            sexo.append('F')
            b = False
        else:
            print("Entrada Inválida!")

    c = True
    while c:
        money = input("Insira o salário do funcionário: ")
        if money.isdigit():
            salario.append(float(money))
            c = False
        else:
            print("Entrada Inválida!")

    if int(age) == 0:
        lock = False


nome.pop(len(nome)-1)
idade.pop(len(idade)-1)
sexo.pop(len(sexo)-1)
salario.pop(len(salario)-1)


m = 0
men = 0
w = 0
women = 0
for i in range(0,len(nome)):
    
    if sexo[i] == 'M':
        men += salario[i]
        m += 1
    if sexo[i] == 'F':
        women += salario[i]
        w += 1

best = 0
for i in range(0,len(nome)):
    if idade[i] < 30:
        if salario[i] > best:
            best = salario[i]

print("\n A média salarial dos homens é %6.2f"%(men/m))
print("\n A média salarial das mulheres é %6.2f"%(women/w))
print("")
print("O melhor salário é %6.2f"%(best))
