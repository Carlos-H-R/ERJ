#include <stdio.h>

int main() {
    int vet1 [10] = {1,2,3,4,5,6,7,8,9,0};
    int vet2 [10] = {0,0,0,0,0,0,0,0,0,0};

    int i = 0;

    while (vet1[i] != 0){
        vet2[i] = vet1[i];
        i++;
    }

    for (i=0; i<10; i++){
        printf("%d\n",vet2[i]);
    }

    return 0;
}
