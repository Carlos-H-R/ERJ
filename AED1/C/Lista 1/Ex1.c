#include <stdio.h>
#define max 3

typedef struct{
    char sex;
    int eye;
    int hair;
    int age;
}dados;

void read(int i,dados v[]){
    printf("\n\nInsira os dados do habitante %d",i+1);
    printf("\nSexo: ");
    fflush(stdin);
    scanf("%c",&v[i].sex);
    printf("Cor dos Cabelos: ");
    scanf("%d",&v[i].hair);
    printf("Cor dos Olhos: ");
    scanf("%d",&v[i].eye);
    printf("Idade: ");
    scanf("%d",&v[i].age);
}

int analise(dados vet[]){
    int i,count = 0;
    int f = 'f';
    for(i=0;i<max;i++){
        if((vet[i].sex == f)&&(18 <= vet[i].age <= 35)&&(vet[i].eye == 2)&&(vet[i].hair == 1))
        {count += 1;}
    }
    return count;
}

int main(){
    dados hab[max];
    int n, result;
    printf("Ao preencher atente para as seguintes entradas\n\n" 
            "Sexo: (1 - feminino / 2 - masculino / 3 - outro\n"
            "Cor dos Cabelos: (1 - louros / 2 - pretos / 3 - castanhos\n "
            "Cor dor Olhos: (1 - azuis / 2 - verdes / 3 - castanhos\n");
    for(n=0;n<max;n++){read(n,hab);}
    result = analise(hab);
    printf("\n\nHa %d pessoa que se encaixam na descricao.",result);
    return 0;
}

//Descrição -> Fem / Olho Verde / Cabelo Louro / Entre 18 e 35