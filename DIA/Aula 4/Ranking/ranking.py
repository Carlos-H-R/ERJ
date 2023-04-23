t = int(input())

for i in range(t):
    n,k = map(int,input().split())
    if (n == k):
        print(1)
    
    else:
        base = 1
        
        for i in range(n,k,-1):
            base *= i
            
            if (base > 1000000007):
                base = base % 1000000007
        
        print(base)
