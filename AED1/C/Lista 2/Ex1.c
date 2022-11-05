#include <stdio.h>
#define max 20

int SeqSearch(int n, int vet[]){
    int i,c;
    printf("\nInsira o valor a ser procurado: ");
    scanf("%d",&c);
    for(i=0;i<n;i++){
        if(vet[i]==c){
            printf("Valor %d encontrado na posicao %d");
            return i;}
    }
    printf("Valor não encontrado!");
    return -1;
}

void fill(int n, int vet[]){
    int i;
    for(i=0;i<n;i++){
        printf("Posicao %d: ",i+1);
        scanf("%d",&vet[i]);
    }
}

int main(){
    int vetor[max];
    fill(max,vetor);
    SeqSearch(max,vetor);
    return 0;
}