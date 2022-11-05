#include <stdio.h>
#include <stdlib.h>

typedef struct lista{
    long cod;
    char desc[140];
    float price;
    struct lista *prev;
    struct lista *next;
}lista;

lista *first;
lista *last;

void startlist(){
    first = NULL;
    last = NULL;
}

int empty(){
    if(first==NULL){return 1;}
    else{return 0;}
}

void show(lista *no){
    printf("\nCodigo: %d",no->cod);
    printf("\nDescricao: %s",no->desc);
    printf("\nPreco: R$%.2f\n",no->price);
}

void input(lista *no){
    printf("\nCodigo: ");
    scanf("%d",&no->cod);
    printf("Descricao: ");
    fflush(stdin);
    scanf("%s",&no->desc);
    printf("Preco: ");
    scanf("%f",&no->price);
}

void read(){
    lista *aux;
    aux = first;
    if(!empty()){
        while(aux!=NULL){
            show(aux);
            aux = aux->next;
        }
    }
    else{printf("\nLista Vazia!\n");}
}

void erase(){
    long value;
    printf("\nCodigo do item a ser removide: ");
    scanf("%d",&value);
    if(empty()){
        lista *aux;
        aux = first;
        while(aux!=NULL){
            if(aux->cod == value){
                aux->prev->next = aux->next;
                aux->next->prev = aux->prev;
                free(aux);
                aux = NULL;
                }
            else{aux = aux->next;}
        }
    }
    else{printf("\nLista Vazia!\n");}
}

void search(){
    long value;
    printf("\nCodigo procurado: ");
    scanf("%d",&value);
    if(empty()==0){
        lista *aux;
        aux = first;
        while(aux!=NULL){
            if(aux->cod == value){show(aux);aux=NULL;}
            else{aux = aux->next;}
        }
        if()printf("\nCodigo nao encontrado!\n");
    }
    else{printf("\nLista Vazia!\n");}
}

void insert(){
    lista *aux;
    aux = (lista*)malloc(sizeof(lista));
    input(aux);
    if(empty()){
        aux->prev = NULL;
        aux->next = NULL;
        first = aux;
        last = aux;
    }
    else{
        first->prev = aux;
        aux->next = first;
        aux->prev = NULL;
        first = aux;
    }
}

void insertafter(){
    lista *aux;
    aux = (lista*)malloc(sizeof(lista));
    input(aux);
    if(empty()){
        aux->prev = NULL;
        aux->next = NULL;
        first = aux;
        last = last;
    }
    else{
        last->next = aux;
        aux->prev = last;
        aux->next = NULL;
        last = aux;
    }
}

int main(){
    startlist();
    int c=-1;
    do{
        printf("\n\nMENU                        \n");
        printf("1 - Inser no inicio             \n");
        printf("2 - Inser no final              \n");
        printf("3 - Mostrar a lista completa    \n");
        printf("4 - Buscar um codigo na lista   \n");
        printf("5 - Excluir um item da lista    \n");
        printf("0 - Encerrar o programa         \n");
        printf("--> ");
        scanf("%d",&c);
        switch(c){
            case 1:
                insert();
            break;
            case 2:
                insertafter();
            break;
            case 3:
                read();
            break;
            case 4:
                search();
            break;
            case 5:
                erase();
            break;
            case 0:
                printf("Finalizando o programa!");
            break;
            default:
                printf("Opcao invalida!");
        }
    }while(c!=0);
    return 0;
}