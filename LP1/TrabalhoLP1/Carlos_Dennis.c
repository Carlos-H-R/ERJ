//Carlos Ribas 
//Dennis Lemos

#include <stdio.h>
#include <stdlib.h>
#define max 3

typedef struct{
    long cod;
    char desc[140];
    float price;
}list;

int list_size(FILE *arquivo){
    list aux;
    int count=0;
    while(fread(&aux,sizeof(list),1,arquivo)){
        count++;
    }
    return count;
}

void insert(FILE *arquivo){
    if(list_size(arquivo)<max){
        list aux;
        printf("\nInsira o codigo: ");
        scanf("%d",&aux.cod);
        printf("Insira a descricao: ");
        fflush(stdin);
        scanf("%s",&aux.desc);
        printf("Inira o preco: ");
        scanf("%f",&aux.price);
        fwrite(&aux,sizeof(list),1,arquivo);
    }
    else{printf("\nLista Cheia!\n");}
}

void printlist(FILE *arquivo){
    list aux;
    if(fread(&aux,sizeof(list),1,arquivo)){
        rewind(arquivo);
        while(fread(&aux,sizeof(list),1,arquivo)){
            printf("\n\nInsira o codigo: %d",aux.cod);
            printf("\nInsira a descricao: %s",aux.desc);
            printf("\nInira o preco: R$%.2f\n",aux.price);
        }
    }
    else{printf("\nLista Vazia!\n");}
}

int main(){
    FILE *arq;
    arq = fopen("Produtos.bin","a+b");
    if(arq!=NULL){
        printf("Abrindo arquivo...\n");
        int c;
        do{
            printf("\n\nMENU:                    \n");
            printf("1 - Inserir novo produto     \n");
            printf("2 - Exibir lista de produtos \n");
            printf("3 - Sair                     \n");
            printf("--> ");
            scanf("%d",&c);
            switch(c){
                case 1:
                    insert(arq);
                break;
                case 2:
                    rewind(arq);
                    printlist(arq);
                break;
                case 3:
                    printf("Programa Encerrado!");
                break;
                default:
                    printf("Comando Invalido!");
                break;
            }
        }while(c!=3);
        return 0;
        }
    else{printf("ERRO! Arquivo não foi aberto!");return 0;}
}