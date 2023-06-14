#include <stdio.h>

typedef struct{
    int x;
    int y;
}ponto;

int main() {
    ponto coordenadas[10];
    int l,a;
    int t,n;
    scanf("%d",&t);

    for (int i=0; i<t; i++){
        scanf("%d %d", &l, &a);
        scanf("%d",&n);
        for (int j=0; j<n; j++){
            scanf("%d %d",coordenadas[j].x,coordenadas[j].y);
        }
    }

    for (int k=0; k<n; k++){
        printf("%d %d\n",coordenadas[k].x,coordenadas[k].y);
    }

    return 0;
}