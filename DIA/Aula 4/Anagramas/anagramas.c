#include <stdio.h>
#include <stdlib.h>

int main() {
    int t,k;
    int* vector;
    scanf("%d",&t);

    for (int i=0; i<t; i++){
        scanf("%d",&k);
        vector = malloc(k*sizeof(int));

        for (int j=0; j<k; j++) scanf(" %d",vector[j]);
        

        //desenvolve
    }

    return 0;
}