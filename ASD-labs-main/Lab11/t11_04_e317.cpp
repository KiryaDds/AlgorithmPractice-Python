#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int karatsuba(int x, int y) {
    if (to_string(x).length() == 1 || to_string(y).length() == 1) {
        return x * y;
    }

    int n = max(to_string(x).length(), to_string(y).length());
    int half = n / 2;
    int x1 = x / (int)pow(10, half);
    int x0 = x % (int)pow(10, half);
    int y1 = y / (int)pow(10, half);
    int y0 = y % (int)pow(10, half);

    int z0 = karatsuba(x0, y0);
    int z2 = karatsuba(x1, y1);
    int z1 = karatsuba(x0 + x1, y0 + y1) - z0 - z2;
    int z = z2 * pow(10, 2 * half) + z1 * pow(10, half) + z0;
    return z;
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << karatsuba(a, b) << endl;
    return 0;
}
