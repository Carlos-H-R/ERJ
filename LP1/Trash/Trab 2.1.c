#include <stdio.h>

void readmat(int n, double vet[][n]){
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<0;j++){
			printf("Elemento (%d,%d): %f",i+1,j+1,vet[i][j]);
		}
	}
}

void FillMat(int n, double vet[][n]){
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			printf("\nElemento (%d,%d): ",i+1,j+1);
			scanf("%f",&vet[i][j]);
		}
	}
}

void copyMat(int n, double vet1[][n], double vet2[][n]){
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			vet1[i][j] = vet2[i][j];
		}
	}
}

float det3(int n, double vet[][n]){
	int i,j,c;
	double temp[3][5];
	copyMat(3,temp,vet);
	for(i=0;i<2;i++){
		for(j=0;j<3;j++){
			temp[i][j+3] = vet[i][j];
		}
	}
	ReadMat(n,vet);
	float det=0;
	for(i=0;i<3;i++){
		det += temp[0][i]*((temp[1][i+1]*temp[2][i+2])-(temp[1][i+2]*temp[2][i+1]));
		printf("%f",det);
	}
	return det;
}

int main(){
	int dim;
	float resultado;
	printf("Insira o tamanho da matriz: ");
	scanf("%d",&dim);
	double mtx[dim][dim];
	FillMat(dim,mtx);
	readmat(dim,mtx);
	resultado = det3(dim,mtx);
	printf("\n\nO determinante da matriz e: %f",resultado);
	return 0;
}
