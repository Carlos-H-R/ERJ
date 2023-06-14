#include <stdio.h>

int main() {
    long int n,m;
    int t;
    long long int rect;
    scanf("%d",&t);

    for (int i=0; i<t; i++) {
        scanf("%d %d",&n,&m);
        rect = 0;
        
        for (int i=1; i <= n; i++){
            for (int j=1; j <= m; j++){
                rect += (n-i+1)*(m-j+1);
            }
        }

        printf("%lld\n",rect);
    }

    return 0;
}