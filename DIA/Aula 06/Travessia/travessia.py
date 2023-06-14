def bridge_cross(position,size,step_range,tempos,memo):
    if (position == size-1):
        return tempos[size-1]
    
    elif (position >= size):
        return 0
    
    elif (memo[position] != -1):
        # Result is already stored in memo
        return memo[position]

    else:
        # Result not stored, the calculation must be done

        # Look at each step possibility and check which gives the smallest time
        # After finding it, the result is stored in memo
        # The result is returned by the function
        
        test = []
        for i in step_range:
            if (position+i) < size:
                local_max = max(tempos[position:position+i])
            else:
                local_max = max(tempos[position:])

            test.append(local_max + bridge_cross(position+i,size,step_range,tempos,memo))

        memo[position] = min(test)

        return memo[position]



t = int(input())
 
for i in range(t):
    n,k = map(int,input().split())
    tempos = list(map(int,input().split()))

    #The array memo stores the smallest time you can have from the current position onward
    memo = [-1]*n
    memo[n-1] = tempos[n-1]
    step_range = list(range(k,0,-1))
    print(bridge_cross(0,n,step_range,tempos,memo))
