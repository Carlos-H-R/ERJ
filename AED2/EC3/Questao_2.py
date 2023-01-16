def GeraSub(ns, t):
    for i in range(t,n):
        S[ns] = V[i]

        if (sum(S) % 2) != 0:
            print(*S)

        if (i < n):
            GeraSub(ns+1,i+1)

V = []
n = int(input("Tamanho do conjunto: "))
S = [0]*n
for i in range(n):
    V.append(int(input("--> ")))

GeraSub(0,0)


[1,2,3]
[1], [1,2], [1,2,3], [2], [2,3], [3]