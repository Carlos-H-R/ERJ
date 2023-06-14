#include <stdio.h>

int main(){
    long int k;
    
    int t;
    scanf("%d",&t);

    int base[10];
    base[0] = 1;
    base[1] = 2;
    base[2] = 2;


    for (int i=0; i<t; i++){
        scanf("%d",&k);

        if (k<4){
            printf("%d\n",base[k-1]);
        }
        else{
            int position = 2;
            int next = 3;
            long int count = 3;

            while(count <= k){
                position++;
                count += base[position-1];

                for (int j=next; j<next+base[position]; j++){
                    base[j] = position;
                }

                next = next + base[position];
            }

            printf("%d\n",base[position]);
        }
    }

    return 0;
}
