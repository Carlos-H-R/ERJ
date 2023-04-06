#include <stdio.h>
#include <stdbool.h>

int main(){
    int t;
    int a,b,area;
    int maior, menor, lado;
    bool test = true;
    scanf("%d",&t);

    for (int i=0; i<t; i++){
        scanf("%d %d",&a,&b);

        if (a > b){
            maior = a;
            menor = b;
            lado = b;
        }

        else{
            maior = b;
            menor = a;
            lado = a;
        }

        area = a*b;

        while (((4*lado*lado) > area) || (test)){
            if (4*lado <= maior){
                test = false;
            }

            else if ((2*lado <= menor) && (2*lado <= maior)){
                test = false;
            }

            else {
                test = true;
                lado--;    
            }
        }
        
        printf("%d\n", lado);
    }

    return 0;
}