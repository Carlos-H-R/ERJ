#include <stdio.h>

int main(){
	float a,b,c;
	
	printf("\nInsira o lado a: ");
	scanf("%d",&a);
	printf("\nInsira o lado b: ");
	scanf("%d",&b);
	printf("\nInsira o lado c: ");
	scanf("%d",&c);
	
	if ((a!=b)&&(a!=c)&&(b!=c))
		printf("O triangulo e Escaleno");
	else if ((a==b)&&(a==c)&&(b==c))
		printf("O triangulo e Equilatero");
	else
		printf("O triangulo e Isosceles");
	return 0;
}
