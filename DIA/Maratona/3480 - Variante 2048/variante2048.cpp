#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void folding(vector<int> &vector, int limit){
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
            vector.erase(vector.begin()+j+1);
            vector[j] *= 2;
            folded = true;
            j = 0;
        }

        else if (vector[j] >  vector[j+1]){
            j += 1;
            if ((j >= vector.size()) and (folded == false)) {folded = false; j = 0;}
        }
    }
}

int check(vector<int> &vector, int limit){
    for (int i=0; i<vector.size(); i++){
        if (vector[i] == limit) {return 1;}
    }
    return 0;
}

int main(){
    int t, N, count;

    cin >> t;

    for (int i=0; i<t; i++) {
        cin >> N;
        count = 0;

        int pot[N];
        vector <int> modified(N);

        for (int k=0; k<N; k++) (cin >> pot[k]);

        for (int k=0; k<N-2; k++){
            modified.clear();
            copy_n(pot+k,N-k,modified.begin());

            folding(modified,2048);
            cout << modified[0];

            // count += check(modified,2048);
        }
        
        cout << count << "\n";
    }

    return 0;
}