#include <stdio.h>

void main() {
    int t = 1;
    int n,m;
    int menor,maior,area;
    int result;
    // scanf("%d",&t);

    for (int a=0; a<t; a++){
        // scanf("%d %d",&n,&m);
        n = 5;
        m = 91;

        area = m*n;

        if (m > n) {
            maior = m;
            menor = n;
        }

        else {
            maior = n;
            menor = m;
        }

        result = area;

// tem que incluir outras condições
// verificar se o quadrado encaixa no lado menor e no maior além de se encaixa na área
        for (int i=1; i<=menor; i++){
            if ((area % i == 0) && (menor % i == 0) && (maior % i == 0) && (area / (i * i) < result)) (result = (area / (i*i)));
        }

        printf("%d\n", result);
    }
}