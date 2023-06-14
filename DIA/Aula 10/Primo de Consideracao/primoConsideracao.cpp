#include <bits/stdc++.h>

using namespace std;

int PC[200001], C[200001];

long long int modPow(int base, int exp, int mod){
    if (exp == 0) return 1;
    if (exp == 1) return (base % mod);

    long long int temp = modPow(base, exp/2, mod);
    if (exp % 2 == 0) return ((temp * temp) % mod);
    else return ((base * temp * temp) % mod);
}

bool ehNumCarmicheal(int n){
    if (C[n] != n){
        for (int i=2; i<n; i++){
            long long int base = modPow(i,n,n);
            if (base != i) return false;
        }
        return true;
    }

    else return false;
}

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

void geraPrimosConsideracao(int n){
    for (int i=2; i<n+1; i++){
        if (ehNumCarmicheal(i)) (PC[i] = PC[i-1] + 1);

        else (PC[i] = PC[i-1]);
    }
}

int main() {
    PC[0] = 0; PC[1] = 0;

    GeraCrivo(200000);
    geraPrimosConsideracao(200000);

    int t, p, q, result;

    cin >> t;

    for (int i=0; i<t; i++){
        cin >> p >> q;

        result = PC[q] - PC[p-1];
        
        cout << result << "\n";
    }

    return 0;
}