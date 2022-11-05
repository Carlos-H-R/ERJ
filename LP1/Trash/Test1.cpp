#include <stdio.h>

typedef struct ent
{
	char mat[25],name[50];
	float n[5];
};

int main()
{
	int i,j;
	float k,m;
	ent a[3];
	
	for(i=0;i<3;i++)
	{
		k = 0;
		printf("Matricula: ");
		fgets(a[i].mat,25,stdin);
		printf("\nNome: ");
		fgets(a[i].name,50,stdin);
		for(j=1;j<5;j++);
		{
			printf("\nInsira a nota %d: ",j);
			scanf("%f",&a[i].n[j]);
			k = k + a[i].n[j];
		}
		a[i].n[0] = k/4;
		m = m + a[i].n[0];
	}	
	printf("\nMédia da turma e %f",m);
}
