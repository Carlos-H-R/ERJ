#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void folding(vector<int> vector, int limit){
    int j = 0;
    bool folded = false;
    bool over = false;

    while (! over){
        if ((vector[j] == limit) or ((vector.size() == 2) and (vector[0] != vector[1]))) (over = true);

        else if (vector[j] <  vector[j+1]){
            if (not folded) (over = true);

            else {folded = false; j = 0;}
        }

        else if (vector[j] == vector[j+1]){
            vector.erase(1);

        }

        else if (vector[j] >  vector[j+1]){
            j += 1;
            if (j >= vector.size()) {folded = false; j = 0;}
        }
    }
}

int main(){
    int t, N;

    cin >> t;

    for (int i=0; i<t; i++) {
        cin >> N;
        int pot[N];
        vector <int> modified(N);

        for (int k=0; k<N; k++) (cin >> pot[k]);

        copy_n(pot,N,modified.begin());

        cout << pot[1] << endl;
        cout << modified[1] << endl;
        
    }

    return 0;
}