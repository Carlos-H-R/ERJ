#include <stdio.h>

void fillmat(int n, double vet[]){
    int i;
    for(i=0;i<n;i++){
        printf("Valor %d: ",i+1);
        scanf("%f",&vet[i]);
    }
}

int main(){
    double vetor[4];
    int x=4;
    int i;
    fillmat(x,vetor);
    for(i=0;i<x;i++){
        printf("\nElemento %d: %f",i+1,vetor[i])        ;
    }
    return 0;
}