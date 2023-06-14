def tree_size(size,array):
    if (array[size-1] != 0):
        return array[size-1]
    
    else:
        count = 0
        
        for j in range(size//2):
            count += 2 * (tree_size(j-1,array) * tree_size(size-j,array))

        if (size%2 != 0):
            count += tree_size(size//2,array) ** 2

        return count
    

t = int(input())
vector = [0]*35
vector[0:2] = [1,2,5]

for i in range(t):
    n = int(input())
    print(tree_size(n,vector))
