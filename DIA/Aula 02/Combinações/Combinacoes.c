#include <stdio.h>

long long int comb(int n, int p){
    if (p == 0) {
        return 1;
    }

    else {
        return ((comb(n-1,p-1)*n)/p);
    }
}

int main() {
    int n,p;
    
    int t;
    scanf("%d",&t);

    for (int i=0; i<t; i++){
        scanf("%d %d",&n,&p);
        printf("%lld\n",comb(n,p));
    }

    return 0;
}