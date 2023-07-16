#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

int absolut(int a){
    if (a < 0) return (a * (-1));
    else return a;
}

int main() {
    int t, n, d;
    int min_dist[2];

    cin >> t;

    for (int i=0; i<t; i++){
        cin >> n >> d;

        int A[n], D[d];
        vector <int> P;
        
        for (int j=0; j<n; j++) (cin >> A[j]);
        
        for (int j=0; j<d; j++) (cin >> D[j]);

        for (int j=0; j<d; j++){
            min_dist[0] = A[0]; min_dist[1] = absolut(D[j] - A[0]);

            for (int k=1; k<n; k++){
                if (absolut(D[j]-A[k]) < min_dist[1]){
                    min_dist[0] = A[k]; 
                    min_dist[1] = absolut(D[j] - A[k]);
                }

                else if (absolut(D[j]-A[k]) == min_dist[1]){
                    if (A[k] < min_dist[0]){
                        min_dist[0] = A[k]; 
                        min_dist[1] = absolut(D[j] - A[k]);
                    }
                }
            }

            P.push_back(min_dist[0]);
        }

        for (int j=0; j<d-1; j++) (cout << P[j] << " ");
        cout << P[d-1] << "\n";
    }

    return 0;
}