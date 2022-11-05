#include <stdio.h>
#define max 99

void readvet(int n,int v[]){
	int i;
    for(i=0;i<n;i++)
    	printf("%d\n",v[i]);
}

int binarySearch(int n, int v[], int c){

    int inicio=0;
    int fim = n;
    int meio,i;

    for(i=inicio; i <= fim; i++) {
        meio = (inicio+fim)/2;

        if (c>v[meio]){
            inicio=meio;
        }
        else if(c==v[meio]){
            printf("\nO item buscado esta na posicao %d\n",meio+1);
            return 0;
        }

        else {
            fim = meio;
        }

    }

    printf("\nO item buscado nao esta na lista!\n");
    return 0;
}

int selectionSearch(int n, int v[], int c){
    int i;

    for(i=0;i<n;i++){
        if(v[i]==c){
            printf("\nO item buscado esta na posicao %d\n",i+1);
            return 0;
        }
    }

    printf("\nO item buscado nao esta na lista!\n");
    return 0;
}


void selectionSort(int v[], int n){
    int menor, swap;
    int i,j;
    for(i = 0; i < (n - 1); i++){
        menor=i;
        for(j = i + 1; j < n; j++){
            if(v[menor]>v[j])
                menor=j;
                }

    if(menor != i){
        swap=v[i];
        v[i]=v[menor];
        v[menor]=swap;
        }
    }
    for(i = 0;i<n;i++){
        printf("%d ",v[i]);
    }
}



void insertionSort(int v[], int n){
    int temp;
    int i,j;

    for(i=1;i<n;i++){
      temp=v[i];
      j=i-1;

      while((temp<v[j])&&(j>=0)){
         v[j+1]=v[j];
         j=j-1;
      }

      v[j+1]=temp;
   }
   for(i = 0;i<n;i++){
        printf("%d ",v[i]);
    }
}

int main(){
    int i,option;
	int lock=1,quant;
    printf("Insira o tamanho do vetor: ");
    scanf("%d",&quant);
    int vet[max];
    for(i=0;i<quant;i++){
        printf("Digite o elemento %d do vetor: ", i+1);
        scanf("%d",&vet[i]);
	}
	do{
	    printf("\n-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n");
	    printf("1 - Reescrever o vetor 		\n");
	    printf("2 - Mostrar o vetor atual	\n");
	    printf("3 - Buscar por um valor 	\n");
	    printf("4 - Ordenar o vetor 		\n");
	    printf("5 - Encerrar o programa		\n");
	    printf("\n-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n");

	    printf("Digite uma opcao: ");
	    scanf("%d", &option);

	    if(option==1){
	    	int i;
	        printf("\nInsira o tamanho do vetor: ");
	        scanf("%d\n",&quant);
	        for(i=0;i<quant;i++){
	            printf("Digite o elemento %d do vetor: 	", i+1);
	            scanf("%d",&vet[i]);
	    	}
	    }
	    else if(option==2){
	    	if(quant==0)
	    		printf("\nO vetor esta vazio!\n");
	    	else{
	    		readvet(quant,vet);
			}
		}

	    else if(option==3){
	        int key;
	        printf("Escolha o tipo de pesquisa: \n");
	        printf("1 - Binary Search(CUIDADO: O VETOR DEVE ESTAR ORDENADO)			\n");
	        printf("2 - Selection Search		\n");
	        printf("--> ");
	        scanf("%d",&key);

	        if (key==1){
	            int c;
	            printf("Insira o valor a ser procurado: ");
	            scanf("%d", &c);
	            binarySearch(quant,vet,c);
	            }

	        else if (key==2){
	            int c;
	            printf("Insira o valor a ser procurado: ");
	            scanf("%d",&c);
	            selectionSearch(quant,vet,c);
	            }
	    }

	    else if (option==4){
	        int key2;
	        printf("Escolha o tipo de ordenacao: 	\n");
	        printf("1 - Selection Sort				\n");
	        printf("2 - Insertion Sort				\n");
	        scanf("%d",&key2);
	        if (key2==1){
	            selectionSort(vet,quant);
	        }
	        if (key2==2){
	            insertionSort(vet,quant);
	        }
		}
	    else if(option==5){
	    	lock=0;
		}
	}while(lock==1);
	printf("Programa Encerrado!");
	return 0;
}
