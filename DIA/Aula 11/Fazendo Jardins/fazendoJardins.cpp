#include <iostream>
#include <bits/stdc++.h>
#include <math.h>

using namespace std;

const double pi = M_PI;

double areaTriangulo(float s, int l1, int l2, int l3){
    return sqrt(s * (s-l1) * (s-l2) * (s-l3));
}

double areaCirculo(double raio){
    return (pi * raio * raio);
}

int main() {
    int t, a, b, c;
    float R, r, s;
    double A, amarela, violeta, vermelha;

    cin >> t;

    for (int i=0; i<t; i++){
        cin >> a >> b >> c;

        s = (a * b * c) / 2.0;
        A = areaTriangulo(s,a,b,c);

        r = A/s;
        R = (a * b *c) / (4.0 * A);

        cout << A << "\n";
        cout << r << "\n";
        cout << R << "\n";

        vermelha = areaCirculo(r);
        violeta = A - vermelha;
        amarela = areaCirculo(R) - A;

    }

    return 0;
}