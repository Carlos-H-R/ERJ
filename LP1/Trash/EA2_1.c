#include <stdio.h>

int main(){
	int a,b,c,x;
	float r;
	
	x=-1;
	while(x<0){
		printf("Insira o valor de x: ");
		scanf("%d",&x);
	}
	printf("\nInsira o valor de a: ");
	scanf("%d",&a);
	printf("\nInsira o valor de b: ");
	scanf("%d",&b);
	printf("\nInsira o valor de c: ");
	scanf("%d",&c);
	
	if((x%2)==0){
		r = (a+b+c)/3;
		printf("A media aritimetica e %f",r);
	}
	else if(x>10){
		r = (2*a+3*b+4*c)/9;
		printf("A media ponderada e %f",r);
	}
	else{
		printf("Valor de X e incoompativel!");
	}
	return 0;
}
