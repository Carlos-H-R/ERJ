#include <stdio.h>

int fat(int n){
    if(n!=0){return n*fat(n-1);}
    else{return 1;}
}

void read(int n,int vet[]){
    int i;
    for(i=0;i<n;i++){
        printf("Posicao %d: ",i+1);
        scanf("%d",&vet[i]);
    }
}

void op(int n, int vet1[], int vet2[]){
    int i;
    for(i=0;i<n;i++){
        vet2[i] = fat(vet1[i]);
    }
}

void print(int n,int vet[]){
    int i;
    printf("//");
    for(i=0;i<n;i++){
        printf("\n %d",vet[i]);
    }
    printf("//");
}

int main(){
    int vetor[10];
    int mod[10];
    read(10,vetor);
    op(10,vetor,mod);
    return 0;
}

//Para imprimir os vetores usar a função print