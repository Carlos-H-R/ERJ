#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(){
    int a,b,c,d;
    int r;
    
    scanf("%d %d %d %d",&a,&b,&c,&d);

    r = a | b | c | d; 

    // r = a & b & c & d;

    // r = !(a | b) & !(c | d);

    // r = !(a & b) ^ !(c & d);

    printf("Resultado %d",r);

    return 0;
}