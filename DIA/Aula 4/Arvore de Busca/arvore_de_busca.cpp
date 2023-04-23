#include <iostream>
#include <vector>

using namespace std;

int tree_size(int size, long long* array[35]) {
    if (array[size-1] != 0) return *array[size-1];
    
    else {
        int count = 0;

        for (int k=1; k <= size/2; k++) count += 2 * (tree_size(k-1,array) * tree_size(size-k,array));

        count += (size % 2) ? (tree_size(size/2,array) * tree_size(size/2,array)) : 0;

        *array[size] = count;

        return count;
    }
}

int main() {
    static long long vector[35] = {1,2,5};

    int t=1,n=5;
    // cin >> t;

    for(int i=0; i<t; i++){
        // cin >> n;
        cout << tree_size(n,vector) << "\n";
    }

    return 0;
}