//Carlos Ribas 
//Dennis Lemos

#include <stdio.h>
#include <stdlib.h>

typedef struct{
    long cod[10];
    char desc[140];
    float price[10];
}list;

void insert(FILE *arquivo){
    list *aux;
    printf("\nInsira o codigo: ");
    scanf("%d",&aux->cod);
    printf("\nInsira a descricao: ");
    fflush(stdin);
    scanf("%s",&aux->desc);
    printf("\nInira o preco: ");
    scanf("%f",&aux->price);
    fwrite(aux,sizeof(list),1,arquivo);
}

// void printlist(FILE *arquivo){
//     if(node!=NULL){
//         
//     }
//     else{printf("\n\nFim!\n\n");}
// }

int main(){
    FILE *arq;
    arq = fopen("Produtos.bin","a+b");
    if(arq!=NULL){
        printf("Abrindo arquivo...\n");
        // fgets(string,tamanho,arq);
        // fputs(endereço_string,arq);
        int c;
        do{
            printf("MENU:                        \n");
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
                    // if(empty_list()==0){
                    //     printlist(first);
                    // }
                    // else{printf("Lista Vazia!");}
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
