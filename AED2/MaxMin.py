"""In the maxmin argorithm the conditionnal tests will verify if the
elements observed are (the same, neighbours or diferent)

In case they are the same the algorithm will return the corresponding
element in both positions (max and min)

In case they are neighbours, will return which is greater and which 
is smaller.

In case they are none of the above, will compare the first end the middle, the (middle + 1) and the end:

The recurcion occurs in the third conditional test."""


from random import randint as rdi

def maxmin(e,d):
    if e == d:
        return (s[e],s[e]) 

    elif d == e+1:
        if s[e] < s[d]:
            return (s[e],s[d])
        
        else:
            return (s[d],s[e])

    else:
        m = (e+d)//2
        a1,b1 = maxmin(e,m)
        a2,b2 = maxmin(m+1,d)
        return (min(a1,a2),max(b1,b2))


def geravet():
    vet = []

    n = int(input("Insira o tamanho do vetor: "))
    for i in range(n):
        vet.append(rdi(1,300))
    
    return vet

s = geravet()
print(*s)
maior,menor = maxmin(0,len(s)-1)
print(maior,menor)