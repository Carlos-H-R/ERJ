#include <stdio.h>

int mdc(int x, int y){
    if (x == y) return x;

    else return (x > y) ? mdc((x-y),y) : mdc((y-x),x);
}

int mmc(int x, int y) {
    return ((x*y)/mdc(x,y));
}

int main() {
    long long int n;
    int a, b, c, result;
    int t;
    scanf("%d",&t);

    for (int i=0; i<t; i++){
        scanf("%lld %d %d %d", &n, &a, &b, &c);
        result = (n/a) + (n/b) + (n/c);
        result -= (n/mmc(a,b)) + (n/mmc(a,c)) + (n/mmc(b,c));
        result += (n/mmc(mmc(a,b),c));
        printf("%d\n",result);
    }

    return 0;
}