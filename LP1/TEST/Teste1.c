#include <stdio.h>

void readmat(int n,int m, int vet[n][m]){
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			printf("Elemento (%d,%d): %g",i+1,j+1,vet[i][j]);
		}
	}
}

void FillMat(int vet[3][3], int sar[3][5]){
	int i,j;
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			printf("\nElemento (%d,%d): ",i+1,j+1);
			scanf("%f",&vet[i][j]);
			printf("\n%d",*vet[i][j]);
            sar[i][j] = vet[i][j];
			printf("\n%d",*sar[i][j]);
		}
	}
    for(i=0;i<3;i++){
        for(j=0;j<2;j++){
            sar[i][j+3] = vet[i][j];
        }
    }
}

float det3(int vet[3][5]){
	int i,j;
    float det=0;
    for(i=0;i<3;i++){
		printf("\n%d",vet[0][i]);
        det += (vet[0][i]) * (((vet[1][i+1]) * (vet[2][i+2]))-((vet[1][i+2]) * (vet[2][i+1])));
        printf("\n%f",det);
    }
    return det;
}

int main(){
	int mtx[3][3];
    int sar[3][5];

    float resultado;

	FillMat(mtx,sar);

	resultado = det3(sar);
	printf("\n\nO determinante da matriz e: %f\n",resultado);
	return 0;
}