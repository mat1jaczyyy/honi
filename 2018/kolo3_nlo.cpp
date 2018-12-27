#include <cstdio>
using namespace std;
typedef unsigned long long u64;

int pow(int x) {
    return x * x;
}

int main() {
    int n, m, k;
    scanf("%d", &n);
    scanf("%d", &m);
    scanf("%d", &k);

    int x[k], y[k], r[k];
    for (int i = 0; i < k; i++) {
        scanf("%d", &x[i]);
        scanf("%d", &y[i]);
        scanf("%d", &r[i]);
        x[i]--; y[i]--;
    }

    
    bool z[n][m] = {};
    u64 sol = n * m * k;

    for (int i = k - 1; i >= 0; i--) {
        for (int a = x[i] - r[i]; a <= x[i] + r[i]; a++) {
            for (int b = y[i] - r[i]; b <= y[i] + r[i]; b++) {
                if (!z[a][b] && pow(x[i] - a) + pow(y[i] - b) <= pow(r[i])) {
                    z[a][b] = true;
                    sol -= i + 1;
                }
            }
        }
    }

    printf("%lld\n", sol);
}