#include <bits/stdc++.h>
using namespace std;

int C[31700000], P[4000001], rq, nf, np, nfs;
long long int n, q, MF[2][50];

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

void FatoraExp (long long int q) {
    int rq = sqrt(q+0.5);
    MF[0][0] = 0;
    nfs = 0;

    for (int i=1; i <=np; i++) {
        int aux = 0;
        
        while((q % P[i]) == 0) {
            q = q/P[i];
            aux += 1;
        }

        if (aux > 0) {
            MF[0][++nfs] = P[i];
            MF[1][nfs] = aux;
        }

        if (q == 1 || P[i] >= rq) break;  
    }

    if (q != 1) {
        MF[0][++nfs] = q;
        MF[1][nfs] = 1;
    }
}

long long int Totiente(long long int n){
    long long int fi = 1;
    long long int fator;
    int exp;

    if (n == 1) return 0;

    for (int i=1; i<=nfs; i++){
        fator = MF[0][i];
        exp = MF[1][i];
        fi *= pow(fator,exp) - pow(fator,exp-1);
    }
    return fi;
}


int main() {
    long long int in, result;
    int t;

    n = 1000000000000000;  //número máximo que pode ser testado - até 1.000.000.000.000.000
	rq = sqrt(n+0.5);  
    
    GeraCrivo(rq);
    GeraPrimos(rq);
    
    cin >> t;

    for (int i=0; i<t; i++){
        cin >> in;

        FatoraExp(in);
        result = Totiente(in);

        cout << result << "\n";
    }

    return 0;
}
