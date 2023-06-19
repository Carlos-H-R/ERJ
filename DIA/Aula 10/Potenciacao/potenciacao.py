def modPow(base, expo, mod):
    if (expo == 0):
        return 1
    
    temp = modPow(base, expo//2, mod)
    temp = ((temp * temp) % mod)
    if ((expo % 2) == 0):
        return temp
    
    else:
        return ((base * temp) % mod)
    

t = int(input())

for i in range(t):
    a = int(input())
    b = int(input())
    m = int(input())

    result = int(modPow(a,b,m))
    print(result)