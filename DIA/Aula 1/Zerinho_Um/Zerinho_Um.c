#include <stdio.h>

int main(){
    int t;
    int a,b,c;
    scanf("%d",&t);

    for (int i=0; i < t; i++){
        scanf("%d %d %d",&a,&b,&c);

        if ((a == b) && (b == c)){
            printf("0\n");
        }

        else {
            if (b == c){printf("1\n");}
            else if (a == c){printf("2\n");}
            else {printf("3\n");}
        }
    
    }

    return 0;
}