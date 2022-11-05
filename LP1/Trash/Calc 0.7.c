#include <stdio.h>

struct pair{
    int a;
    int b;
};

struct pair getnum(){
    struct pair num;
    printf("\n \nInsira o primeiro numero: ");
    scanf("%d",&num.a);
    printf("\nInsira o segundo numero: ");
    scanf("%d",&num.b);
    return num;
}

int soma(){
    struct pair p;
    p = getnum();
    int r = p.a + p.b;
    printf("\nO resultado da soma e: %d\n",r);
    return 0;
}

int sub(){
    struct pair p;
    p = getnum();
	int r = p.a - p.b;
	printf("\nO resultado da subtracao e: %d\n",r);
	return 0;
}

int mult(){
    struct pair p;
    p = getnum();
	int r = p.a * p.b;
	printf("\nO resultado da multiplicacao e: %d\n",r);
	return 0;
}

int div(){
    struct pair p;
    p = getnum();
    if(p.b==0){
		printf("\nNao permitido divisao por zero!");
	}
	else{
    	int r = (p.a / p.b);
		printf("\nO resultado da divisao e: %d\n",r);    	    
    return 0;
	}
}

int main(){
	int c;
    do{
    	printf("\n\n----------Calculadora------------\n");
    	printf("1 - para somar dois numeros      \n");
    	printf("2 - para subtrair dois numeros   \n");
    	printf("3 - para multiplicar dois numeros\n");
    	printf("4 - para dividir dois numeros    \n");
    	printf("5 - para encerrar a calcualdora  \n");
    	printf("\nInsira seu comando:	");
    	scanf("%d",&c);
    	
    	if(c==1){
            soma();
    	}
    	else if(c==2){
            sub();   	    
    	}
    	else if(c==3){
            mult();     
    	}
    	else if(c==4){
            div();
    	}
    	else if(c==5){
    	    printf("\n\nEncerrando o programa!\n");
    	}
    	else{
    	    printf("Comando invalido!\n");
    	}
    }while(c!=5);
    return 0;
}
