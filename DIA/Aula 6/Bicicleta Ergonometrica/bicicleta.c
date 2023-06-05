#include <stdio.h>
#include <string.h>

void main() {
    int t = 1;
    int T,M,N;

    T = 10;
    M = 5;
    N = 10;
    int total;
    // scanf("%d",&t);

    for (int i=0; i<t; i++){
        // scanf("%d %d %d",&T,&M,&N);
        
        int memo[N-M+2][T];
        memset(memo,-1,(N-M+2)*(T)*sizeof(int));

        total = 0;

        for (int k=0; k<T; k++){
            for (int j=0; j<(N-M+2); j++) {
                if ((j == 0) || (j == N-M+2)) (memo[j][k] = 0);

                else if ((k+1) == 1) (memo[j][k] = 1);

                else (memo[j][k] = memo[j-1][k-1] + memo[j+1][k-1]);            
            }
        }

        for (int m=1; m<N-M+1; m++) (total += memo[m][T-1]);

        printf("%d\n",total);
    }
}