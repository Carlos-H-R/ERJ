def area_celeiro(largura,altura,n_pares,coordenadas):
    pass

t = int(input())

for i in range(t):
    l,a = map(int,input().split())
    coord = list(map(int,input().split()))
    
    n = coord[0]
    coord = coord[1:]

    area_celeiro(l,a,n,coord)
