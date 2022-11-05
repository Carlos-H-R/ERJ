#include <stdio.h>
#include <stdlib.h>

// void fillmtx()
void readmat(double mat[][3]){
    int i,j;
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            printf("\nElemento (%d,%d): %lf",i+1,j+1,mat[i][j]);
        }
    }
}

double det3(double mat[3][3]){
    int i,j;
    double det = 0;
    for(i=0;i<3;i++){
        det += ((mat[0][i%3] * mat[1][(i+1)%3] * mat[2][(i+2)%3]) - (mat[0][(i+2)%3] * mat[1][(i+1)%3] * mat[2][i%3]));
    }
    return det;
}

int main(){
    int dim;
    int i,j;
    double mat[3][3];
    double det;
    printf("MATRIZ 3X3 \n\nVamos encontrar o determinante! \n\n\n");
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            printf("Elemento (%d,%d): ",i+1,j+1);
            scanf("%lf",&mat[i][j]);
        }
    }
    det = det3(mat);
    printf("\n\nO determinante da matriz eh %lf",det);
    return 0;
}