#include <stdio.h>

int main() {
    int k,n;
    int t;
    scanf("%d",&t);

    for (int i=0; i<t; i++){
        long long int base = 1;
        scanf("%d %d",&n,&k);
        
        if (n == k) printf("%d\n",base);

        else{
            for (int j=n; j>k; j--){
                base *= j;

                if (base > 1000000007) base = base % 1000000007;
            }

            printf("%d\n",base);
        }
    }

    return 0;
}