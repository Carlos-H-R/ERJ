t = int(input())

for i in range(t):
    base_case = [1,2,2]
    k = int(input())

    if (k < 3):
        print(base_case[k-1])

    else:
        position = 2

        while(sum(base_case) < k):
            position += 1
            base_case += [position]*base_case[position-1]

        if ((sum(base_case) - k) > base_case[position-1]):
            margem = (sum(base_case) - k)//base_case[position-1]
            print(base_case[len(base_case)-margem])

        else:
            print(base_case[len(base_case)-1])    

        