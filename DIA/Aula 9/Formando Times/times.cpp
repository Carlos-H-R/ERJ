#include <iostream>

using namespace std;

int MDC(int n1, int n2){
    // Calcula MDC

    return 0;
}

int main() {
    int t, a, b, c, d, p;
    cin >> t;

    for (int i=0; i<t; i++){
        cin >> a >> b >> c;
        d = MDC(a,b);
        p = 0;

        if ((c % d) == 0) {
            // com o MDC resuz os coeficientes da equação

            // com o coef reduzidos calcula o num de soluções com a formula

            // também é possível testando soluções
        }

        else cout << p;
    }

    return 0;
}