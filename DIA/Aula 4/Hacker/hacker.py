def arrj(k,n):
    if (n % 2 != 0):
        return (k*arrj(k,n-1)) % 1000000007
    
    elif (n>10000):
        return (arrj(k,n//2) ** 2) % 1000000007
    
    else:
        return (k ** n) % 1000000007

t = int(input())

for i in range(t):
    k,n = map(int,input().split())
    print(arrj(k,n))    
    