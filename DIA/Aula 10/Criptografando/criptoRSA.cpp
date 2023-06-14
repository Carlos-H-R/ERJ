#include <bits/stdc++.h>

using namespace std;
// t = 48  e = 17
// ed = 1 + kt
// e d - t k = 1
// a x - b y = 1

int modInv(int e, int t, int &d, int &k){
    int r, d1, k1; 

    if (t == 0) {
        d = 1; k = 0;
        return e;
    }

    else{
        r = modInv(t, e % t, d1, k1);
        d = k1; k = d1 - (e/t) * k1;
        
        if (r == 1) return r;
    }

    return r;
}

long long int modPow(long long int base, long long int exp, long long int mod){
    if (exp == 0) return 1;
    if (exp == 1) return (base % mod);

    long long int temp = modPow(base, exp/2, mod);
    if (exp % 2 == 0) return ((temp * temp) % mod);
    else return ((base * temp * temp) % mod);
}

int main(){
    long long int t, n, p, q, e, msg;
    int d,k;

    cin >> t;

    for (int i=0; i<t; i++){
        cin >> p >> q >> e;
        cin >> msg;

        t = (p-1) * (q-1);
        n = p * q;

        modInv(e,t,d,k);

        cout << modPow(msg,d,n) << "\n";
    }

    return 0;
}