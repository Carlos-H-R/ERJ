def folding(array,limit):
    j = 0
    folded = False
    over = False

    while not over:
        if (array[j] == limit) or ((len(array) == 2) and (array[0] != array[1])):
            over = True
        
        elif (array[j] < array[j+1]):
            if not folded:
                over = True
            
            else:
                folded = False
                j = 0

        elif (array[j] == array[j+1]):
            array.pop(j+1)
            array[j] *= 2
            folded = True
            j = 0

        elif (array[j] > array[j+1]):
            j += 1
            if (j >= len(array)-1):
                folded = False
                j=0


def check(array,limit):
    for i in array:
        if (i == limit):
            return True
        else:
            return False
    

def check(array,limit):
    for i in array:
        if (i == limit):
            return True

t = int(input())

for i in range(t):
    N = int(input())

    pot = list(map(int,input().split()))

    count = 0

    for j in range(N-2):
        aux = pot[j:].copy()
        folding(aux,2048)
        
        if check(aux,2048):
            count += 1

    print(count)