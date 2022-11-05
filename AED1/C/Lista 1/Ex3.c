#include <stdio.h>
#define max 1

typedef struct{
    char nome[50];
    char raca[10];
    char nasc[15];
    char sexo[10];
}dado;

void read(int n, dado vet[]){
    int i;
    for(i=0;i<n;i++){
        printf("\nAnimal %d",i+1);
        printf("\nNome: ");
        fflush(stdin);
        fgets(vet[i].nome,50,stdin);
        printf("Raca: ");
        fflush(stdin);
        fgets(vet[i].raca,10,stdin);
        printf("Dara de Nascimento: ");
        fflush(stdin);
        fgets(vet[i].nasc,15,stdin);
        printf("Sexo: ");
        fflush(stdin);
        fgets(vet[i].sexo,10,stdin);
    }
}

void print(int n,dado vet[]){
    int i;
    for(i=0;i<n;i++){
        printf("\n\nAnimal %d",i+1);
        printf("\nNome: %s",vet[i].nome);
        printf("Raca: %s",vet[i].raca);
        printf("Dara de Nascimento: %s",vet[i].nasc);
        printf("Sexo: %s",vet[i].sexo);
    }
}

int main(){
    dado animais[max];
    read(max,animais);
    print(max,animais);
    return 0;
}