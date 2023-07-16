#include <stdio.h>

enum tipos_raca {humano, elfo, darf} raca;

typedef struct status {
    int forca;
    int defesa;
    int agilidade;
    int HP;
}status;

typedef struct guerreiro{
    char nome[20];
    enum tipos_raca raca;
    int idade;
    status sts;
    char destreza[30];
    int rage;
}guerreiro;

typedef struct mago{
    enum tipos_raca raca;
    char nome[20];
    int idade;
    status sts;
    int MP;
}mago;


union personagem{
    guerreiro war;
    mago mag;
}personagem;


int main(){
    union personagem p1;
    scanf("Kiron",p1.mag.nome);
    p1.mag.raca = humano;
    p1.mag.idade = 28;
    p1.mag.MP = 12;
    p1.mag.sts.forca = 11;
    p1.mag.sts.defesa = 16;
    p1.mag.sts.agilidade = 9;
    p1.mag.sts.HP = 17;

    printf("%d",p1.mag.MP);

    return 0;
}