#include <stdio.h>

int main() {
    int t;
    int n,k;
    scanf("%d",&t);

    for (int i=0; i<t; i++){
        scanf("%d %d",&n,&k);

        int tempos[n];
        for (int j=0; j<n; j++) scanf("%d",tempos[j]);

        for (int s=0; s<n; s++) printf("%d ",tempos[s]);
    }

    return 0;
}