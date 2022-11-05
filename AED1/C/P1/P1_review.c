#include <stdio.h>
#include <stdlib.h>
#define M 100

typedef struct {
	int id;
	char nome[50];
}no;

typedef struct {
	no valores[M];
	int i,f,n;
}fila;

int fila_vazia(int n){
	if (n==0)
		return 1;
	return 0;
}

int fila_cheia(int n){
	if(n==M)
		return 1;
	return 0;
}

void inicializa_fila(fila *clientes){
	clientes->f=-1;
	clientes->i=-1;
	clientes->n=0;
}

void enfileirar(fila *clientes){
    if(fila_vazia(clientes->n)==1){
        printf("ID: ");
        fflush(stdin);
        scanf("%d",&clientes->valores[(clientes->f)+1].id);
        printf("Nome: ");
        fflush(stdin);
        scanf("%s",&clientes->valores[(clientes->f)+1].nome);
        //fgets(clientes->valores[(clientes->f)+1].nome,50,stdin);
        clientes->i+=1;
        clientes->f+=1;
        clientes->n+=1;
    }
    else if(fila_cheia(clientes->n)==0){
        printf("ID: ");
        fflush(stdin);
        scanf("%d",&clientes->valores[(clientes->f)+1].id);
        printf("Nome: ");
        fflush(stdin);
        scanf("%s",&clientes->valores[(clientes->f)+1].nome);
        //fgets(clientes->valores[(clientes->f)+1].nome,50,stdin);
        clientes->f+=1;
        clientes->n+=1;
    }
    else{
        printf("Fila cheia!");
    }
}


void mostrarprox(fila *clientes){
    if(fila_vazia(clientes->n)==1){
        printf("Fila Vazia!");
    }
    else{
        printf("Proximo da fila: ");
        printf("\nId: %d",clientes -> valores[clientes->i].id);
        printf("\nNome: %s",clientes -> valores[clientes->i].nome);
    }
}


void desenfileirar(fila *clientes){
    int i;
    if((clientes->)==1){
        inicializa_fila(clientes);
    }
    else if(fila_vazia(clientes->n)==1){
        printf("Fila já esta vazia!");
    }
    else{
        for(i=0;i<c-1;i++){
            clientes->valores[i] = clientes->valores[i+1];
        }
        clientes->f-=1;
    }
}


int main(){
	int op;
	fila clientes;
	no c;
	inicializa_fila(&clientes);
	do{
		printf("\n1- Adicionar cliente na fila de atendimento");
		printf("\n2- Atender cliente para compra do ingresso"); //desenfileirar
		printf("\n3- Consultar o próximo cliente a ser antendido");
		printf("\n4- Sair");
		printf("\nO que deseja fazer? ");
		fflush(stdin);
		scanf("%d",&op);
		switch(op){
			case 1:{
				printf("\nCadastro para compra de ingresso\n");
				enfileirar(&clientes);
				break;
			}
			case 2:{
				desenfileirar(&clientes);
				break;
			}
			case 3:{
				mostrarprox(&clientes);
				break;
			}
			case 4:{
				printf("\nSaindo...");
				break;
			}
			default:{
				printf("\nOpção inválida!");
				break;
			}
		}
		//system("Pause");
		//system("cls");
	}while(op!=4);
    return 0;
}