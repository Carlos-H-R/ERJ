#include <iostream>
#include <string>

using namespace std;

int modPow(long long int base, long long int expo, int mod){
    if (expo == 0) return 1;
    if (expo == 1) return (base % mod);

    int temp = modPow(base,expo/2,mod);
    
    if ((expo % 2) == 0) return ((temp * temp) % mod);

    else return ((base * temp * temp) % mod);
}

int hornerBase(int size, string digitos, int mod){
    int m = 0;
    int aux;

    for(int i=0; i<size; i++){
        aux = digitos[i] - '0';

        m = (m*10 + aux) % mod;
    }

    return m;
}

long long int hornerExpo(int base, int size, string digitos, int mod){
    long long int m = 1;
    int aux;

    for (int i=0; i<size; i++){
        aux = digitos[i] - '0';

        m = (modPow(m,10,mod) * modPow(base,aux,mod)) % mod;
    }

    return m;
}

int main() {
    int sizeBase, sizeExpo;
    int t, mod;
    long long int base, result;
    string baseS, expoS;

    cin >> t;

    for (int i=0; i<t; i++){
        cin >> baseS;
        cin >> expoS;
        cin >> mod;

        sizeBase = baseS.size();
        sizeExpo = expoS.size();

        base = hornerBase(sizeBase, baseS, mod);
        result = hornerExpo(base,sizeExpo,expoS,mod);

        cout << result << "\n";
    }

    return 0;
}