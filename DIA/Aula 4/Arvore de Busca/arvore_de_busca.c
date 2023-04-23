#include <stdio.h>

long long int tree_size(int size, long long* array) {
    if (size == 0) return 1;
    
    else if (array[size-1] != 0) return array[size-1];
    
    else {
        long long int count = 0;

        for (int k=1; k <= size/2; k++) count += 2 * (tree_size(k-1,array) * tree_size(size-k,array));

        count += (size % 2) ? (tree_size(size/2,array) * tree_size(size/2,array)) : 0;

        array[size-1] = count;

        return count;
    }
}

int main() {
    static long long possibilities[35] = {1,2,5};
    
    int t, n;
    scanf("%d",&t);

    for (int i=0; i<t; i++){
        scanf("%d",&n);
        printf("%lld\n",tree_size(n,possibilities));
    }

    return 0;
}