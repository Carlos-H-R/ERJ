#include <stdio.h>
#include <stdlib.h>

typedef struct lista_encadeada
{
    int elemento;
    struct lista_encadeada *next;
}lista_encadeada;


int main() {
    lista_encadeada *prt;
    lista_encadeada *init;
    
    prt = malloc(sizeof(lista_encadeada));
    init = prt;

    prt->elemento = 1;
    prt->next = malloc(sizeof(lista_encadeada));
    
    prt = prt->next;

    prt->elemento = 2;
    prt->next = malloc(sizeof(lista_encadeada));

    prt = prt -> next;

    prt->elemento = 3;
    prt->next = malloc(sizeof(lista_encadeada));

    prt = prt -> next;

    prt->elemento = 4;
    prt->next = NULL;

    // prt = init;

    // for (int i=0; i<4; i++) {
    //     printf("%d ",prt->elemento);
    //     prt = prt->next;
    // }
    
    free(init);
    free(prt);

    return 0;
}