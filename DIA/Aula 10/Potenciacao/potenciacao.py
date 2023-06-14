def modPow(base, expo, mod):
    if (expo == 0):
        return 1
    
    if (expo == 1):
        return (base % mod)
    
    temp = modPow(base, expo//2, mod)
    if ((expo % 2) == 0):
        return ((temp * temp) % mod)
    
    else:
        return ((base * temp * temp) % mod)
    

t = int(input())

for i in range(t):
    a = float(input())
    b = float(input())
    m = float(input())

    result = int(modPow(a,b,m))
    print(result)