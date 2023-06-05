#include <bits/stdc++.h>
using namespace std;

int C[31700000], P[4000001], S[10000001], rq, nf, np, nd;
long long int n, q, F[50], D[10000];
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

bool TestaPrimo (long long int q) {
    return (C[q] == q);
}

bool EhSuperPrimo(long long int super) {
    long long int k = log10(super);
    long long int mod = super;
    int resto;
    
    do {
        resto = (mod % 10);
        mod = (resto * pow(10,k)) + (mod / 10);

        if (!TestaPrimo(mod)) return false;
    } while (mod != super);

    return true;
}

void SuperPrimos(long long int n){
    S[0] = 0; S[1] = 0;
    
    for (int i=2; i<n; i++){
            if (EhSuperPrimo(i)) S[i] = S[i-1] + 1;

            else S[i] = S[i-1];
    }
}

int main() {
    int t, v, b, aux;
    int result;
    long long in;
    
    n = 1000000000000000; 
	rq = sqrt(n+0.5); 

    GeraCrivo(rq);
    SuperPrimos(10000001);

    cin >> t;

    for (int i=0; i<t; i++){
        result = 0;
        aux = 1;
        
        cin >> v >> b;

        result = S[b] - S[v-1];

        cout << result << "\n";
    }

    return 0;
}
