def folding(array,limit):
    j = 1
    folded = False
    over = False
    modified = array.copy()
    while (not over):
        if (modified[j] == modified[j-1]):
            modified.pop(j)
            modified[j-1] *= 2
            folded = True

        else:
            j += 1

        if (j >= len(modified)) or (modified[j] == limit):
            over = True

    if folded:
        return folding(modified,limit)
    
    else:
        return modified
    

def check(array,limit):
    for i in array:
        if (i == limit):
            return True

t = int(input())

for i in range(t):
    N = int(input())

    pot = list(map(int,input().split()))

    count = 0

    for j in range(N-1):
        aux = folding(pot[j:],2048)
        if check(aux,2048):
            count += 1

    print(count)