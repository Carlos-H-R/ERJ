#include <stdio.h>

int prog(int nivel, int minuto, int M, int N, int memo[N][]){
    if ((nivel < M) || (nivel > N)) return 0;

    else if (minuto == 1) return 1;

    else if (memo[nivel][minuto] != -1) return (memo[nivel[minuto]]);

    else return (prog(nivel-1,minuto-1,M,N, memo) + prog(nivel+1,minuto-1,M,N, memo));
}

void main() {
    int t;
    int T,M,N;
    int total;
    scanf("%d",&t);

    for (int i=0; i<t; i++){
        scanf("%d %d %d",&T,&M,&N);
        int memo[N][T];
        total = 0;

        for (int j=0; j<M; j++) memo[j][T-1] = prog(j,T,M,N,memo);

        for (int k=M; k<N; k++) (total += memo[k][T-1]);

        printf("%d\n",total);
    }
}