#include <stdio.h>
#include <math.h>

long long int arrj(long long int k, int n){
    if (n % 2 != 0) return ((k * arrj(k,n-1)) % 1000000007);

    else if (n > 10000) {
        long long int aux = arrj(k,n/2);
        aux = (aux * aux);
        if (aux > 1000000007) (aux % 1000000007);
        return aux;
    }

    else {
        long double power = pow(k,n);
        power = round(power);

        if (power > 1000000007) {
            long long int aux = ((int) power) % 1000000007; 
            return aux;       
        }

        long long int aux = round(power);
        return aux;
    }
}

int main() {
    int t,k,n;
    // scanf("%d",&t);
    t = 1;

    for (int i=0; i<t; i++){
        k = 10;
        n = 100;
        // scanf("%d %d",&k,&n);

        printf("%d\n",arrj(k,n));
    }

    return 0;
}