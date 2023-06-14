#include <bits/stdc++.h>
using namespace std;

int C[31700000], P[4000001], rq, nf, np, nd;
long long int n, q, F[50], D[10000];
bool teste;

void GeraCrivo (int n)
{    int i, rq, t, d;
     for (i=1; i<=n; i++)   C[i] = i;
     for (i=2; i<=n; i+=2)  C[i] = 2;
     rq = sqrt(n+0.5);
     for (i=3; i<=rq; i+=2)
     {   if (C[i] == i)
         {   t = i*i;  d = i+i;
             while(t<=n)
             {   if (C[t] == t) C[t] = i;
                 t = t+d;
             }
         }
     }
}
void GeraPrimos (int rq)
{    np=0;
     for (int i=2; i<=rq; i++)
         if (C[i]==i)  P[++np]= i;
}

bool TestaPrimo (long long int q)
{    bool primo = true;
     for (int i=1; i<=np; i++)
     {   if ((q % P[i]) == 0)
         {   if (q != P[i]) primo = false;
             break;
         }    
     }
     return (primo);
}

int main() {
    int t;
    long long in;
    
    n = 1000000000000000; 
	rq = sqrt(n+0.5); 

    GeraCrivo(rq);
    GeraPrimos(rq);

    cin >> t;

    for (int i=0; i<t; i++){
        cin >> in;

        if (TestaPrimo(in)) (cout << "N\n");

        else (cout << "S\n");
    }

    return 0;
}
