import numpy as np


def mmq_cn(x,y,gr):
  sx=np.max(x.shape)
  sy=np.max(y.shape)
  x=x.reshape(sx,1) # coloca como vetor em pé
  y=y.reshape(sy,1) # coloca como vetor em pé
  gr=np.sort(np.unique(gr)) # elimina os graus repetidos e coloca em ordem crescente
  maxdimgr=np.max(gr.shape)
  g=np.zeros([sx,maxdimgr])
  for ii in range(maxdimgr):
    g[:,ii:ii+1]=np.power(x,gr[ii]) # constroi a matriz de mínimos quadrados
  coef=np.linalg.solve(np.transpose(g)@g,np.transpose(g)@y) # resolve o sistema linear AtAx=Aty

  x=np.sort(np.unique(x)) # elimina os pontos do domínio repetidos e coloca em ordem crescente
  sx=np.max(x.shape)
  x=x.reshape(sx,1) # coloca como vetor em pé
  sol=np.zeros([sx,1])
  for ii in range(maxdimgr):
    sol=sol+coef[ii]*np.power(x,gr[ii]) # calcula as imagens usando o polinômio
  coefc=np.zeros([np.max(gr)+1,1]) # inicializo todos os coeficientes como nulos
  for ii, deg in enumerate(gr): # uso dois contadores fornecidos pela função enumerate
    coefc[deg]=coef[ii] # atualizo apenas os coeficientes  dos graus do vetor de entrada gr, como o Python

  return x, sol, coefc, gr


x = list(map(float,input().split()))
y = list(map(float,input().split()))
g = list(map(int,input().split()))


for i in range(len(x)):
  x[i] = [x[i]]

for i in range(len(y)):
  y[i] = [y[i]]

x = np.array(x)
y = np.array(y)
g = np.array(g)


[xx, sol, coefc, gr] = mmq_cn(x,y,g)

print("x = \n",xx)
print("\nSolucao = \n",sol)
print("\nCoeficientes = \n",coefc)
print("\nGraus = \n",gr)
