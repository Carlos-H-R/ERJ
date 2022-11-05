#include <stdio.h>
#include <stdlib.h>

typedef struct{
    long cod;
    char desc[140];
    float price;
    struct list *next;
}list;
list *first;

void start_list(){
    first = NULL;
}

int empty_list(){
    if(first==NULL)
        return 1;
    return 0;
}

void insert_first(){
    list *aux;
    printf("\nInsira o codigo: ");
    scanf("%d",aux->cod);
    printf("\nInsira a descricao: ");
    fflush(stdin);
    scanf("%s",aux->desc);
    printf("\nInira o preco: ");
    scanf("%f",aux->price);
    aux->next = first;
    first = aux;
}

void insert_last(){
    list *aux;
    printf("\nInsira o codigo: ");
    scanf("%d",aux->cod);
    printf("\nInsira a descricao: ");
    fflush(stdin);
    scanf("%s",aux->desc);
    printf("\nInira o preco: ");
    scanf("%f",aux->price);
}

void printlist(list *node){
    if(node!=NULL){
        printf("\n\nCodigo: %d",node->product.cod);
        printf("\nDescricao: %s",node->product.desc);
        printf("\nPreco: R$%.2f",node->product.price);
        printlist(node->next);
    }
    else{printf("\n\nFim!\n\n");}
}

int main(){
    int d,c=0;
    start_list(first);
    while(c!=3){
        printf("MENU:                        \n");
        printf("1 - Inserir novo produto     \n");
        printf("2 - Exibir lista de produtos \n");
        printf("3 - Sair                     \n");
        printf("--> ");
        scanf("%d",&c);
        switch(c){
            case 1:
                printf("\nInserir: ");
                printf("\n1 - Inicio \n2 - Fim\n");
                prinft("--> ")
                scanf("%d",&d);
                if(d==1){insert_first();}
                else if(d==2){insert_last();}
                else{printf("Comando Invalido!");}
            break;
            case 2:
                if(empty_list()==0){
                    printlist(first);
                }
                else{printf("Lista Vazia!");}
            break;
            case 3:
                printf("Programa Encerrado!");
            break;
            default:
                printf("Comando Invalido!");
            break;
        }
    }
}