#include <iostream>
using namespace std;

int main(){
    int n,k,t;
    cin >> t;

    for (int i=0; i<t; i++){
        long long int base = 1;
        cin >> n >> k;

        if (n != k) {
            for (int j=n; j>k; j--){
                base *= j;

                if (base > 1000000007) base = base % 1000000007;
            }
        }

        cout << base << "\n";
    }
}