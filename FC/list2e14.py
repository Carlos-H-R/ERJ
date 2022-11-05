n = int(input('Digite o número de termos da sequência: '))

sr = 0

for i in range(1,n+1):
    sr += ((-1)**(1+i))*(1/(i**2))

pi = (12*sr)**(1/2)

print('O valor aproximado de Pi usando %i termos é %f'%(n,pi))

input('Pressione qualquer tecla para finalizar')
