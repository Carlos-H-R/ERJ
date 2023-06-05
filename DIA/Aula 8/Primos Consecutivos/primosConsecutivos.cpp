#include <bits/stdc++.h>
using namespace std;

int C[31700000], P[4000001], rq, nf, np, nd, nfs;
long long int n, q, F[50], D[10000], MF[2][50];
bool teste;

void GeraCrivo (int n) {
    int i, rq, t, d;
    for (i=1; i<=n; i++)   C[i] = i;
    for (i=2; i<=n; i+=2)  C[i] = 2;
    rq = sqrt(n+0.5);
    for (i=3; i<=rq; i+=2) {
        if (C[i] == i) {
            t = i*i;  d = i+i;
            while(t<=n) {
                if (C[t] == t) C[t] = i;
                t = t+d;
            }
        }
    }
}

void GeraPrimos (int rq) {
    np=0;
    for (int i=2; i<=rq; i++)
        if (C[i]==i)  P[++np]= i;
}

int PrimosConsecutivos(long long int N){
    long long int beg, end, soma;
    int num = 0;
    beg = 1; end = 1;
    soma = P[beg];

    while ((P[beg] <= N) && (P[end] <= N)){
        if (beg > end) break;
        
        else if (soma < N) {
            end++;
            soma += P[end];
        }

        else if (soma > N) {
            soma -= P[beg];
            beg++;
            }

        else if (soma == N){
            soma -= P[beg];
            num++; 
            beg++;}
    }
    
    return num;
    // Encerra se o primeiro for maior q N
    // Se a soma for menor q N avança end
    // Se a soma for maior q N avança beg
}

int main() {
    long long int result, N;
    int t;

    n = 1000000000000000;  //número máximo que pode ser testado - até 1.000.000.000.000.000
	rq = sqrt(n+0.5);  
    
    GeraCrivo(rq);
    GeraPrimos(rq);
    
    cin >> t;

    for (int i=0; i<t; i++){
        cin >> N;

        result = PrimosConsecutivos(N);

        if ((result % 2) == 0) (cout << "Bruno\n");
        
        else (cout << "Joana\n");
    }

    return 0;
}
