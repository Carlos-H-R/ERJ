t = int(input())

for a in range(t):
    T,M,N = map(int,input().split())
    total = 0

    memo = [1]*(N-M+1)
    memo = [0] + memo + [0]

    if (T>1):
        for k in range(T):
            aux = []
            for j in range(1,N-M+2):
                result = (memo[j-1] + memo[j+1]) % 1000000007
                aux.append(result)
            memo = [0] + aux + [0]
        
    # memo = []
    # for k in range(0,T):
    #     memo.append([])
    #     for j in range(0,(N-M+3)):
    #         if ((j == 0) or (j == N-M+2)):
    #             memo[k].append(0)

    #         elif (k == 0):
    #             memo[k].append(1)

    #         else:
    #             memo[k].append((memo[k-1][j-1] + memo[k-1][j+1]) % 1000000007)

    print(memo)
    print(sum(memo))
            