#include <stdio.h>

typedef struct lista{
    int info;
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

void show(){
    printf("\n\n%d\n\n",first->info);
}

void read(lista *no){
    int tempinfo;
    printf("Insira a informacao: ");
    scanf("%d",&tempinfo);
    no->info = tempinfo;
}

void insert(){
    lista *aux;
    read(aux);
    if(empty()==1){
        aux->prev = NULL;
        aux->next = NULL;
        first = aux;
        last = aux;
        show();
    }
    else{
        first->prev = aux;
        aux->next = first;
        first = aux;
    }
}

void insertafter(){
    lista *aux;
    read(aux);
    if(empty()==1){
        aux->prev = NULL;
        aux->next = NULL;
        first = aux;
        last = last;
    }
    else{
        last->next = aux;
        aux->prev = last;
        last = aux;
    }
}

int main(){
    startlist();
    int c=0;
    do{
        printf("MENU\n");
        printf("1 - insere no inicio\n");
        printf("2 - insere no final \n");
        printf("3 - mostra primeiro item da lista\n");
        printf("4 - encerra o programa\n");
        printf("--> ");
        scanf("%d",&c);
        switch(c){
            case 1:
                insert();
            break;
            case 2:
                insert();
            break;
            case 3:
                show();
            break;
            case 4:
                printf("Finalizando o programa!");
            break;
            default:
                printf("Opcao invalida!");
        }
    }while(c!=4);
    return 0;
}
