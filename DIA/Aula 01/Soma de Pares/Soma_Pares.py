t = int(input())

for j in range(t):
    n,s = map(int,input().split())
    numbers = list(map(int,input().split()))

    count = 0
    i = 0
    f = n-1

    while(i != f):
        if ((numbers[i]+numbers[f]) == s):
            count += 1
            i += 1

        elif ((numbers[i]+numbers[f]) < s):
            i += 1

        else:
            f -= 1

    print(count)
