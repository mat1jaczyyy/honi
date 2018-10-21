#include <cstdio>
#include <algorithm>
using namespace std;

int n, m;
int a[100000], b[100000];
int* x = &a[0];
int* y = &b[0];

int abs(int _, int __) {
    if (_ < __) {
        return __ - _;
    }
    return _ - __;
}

int main() {
    scanf("%d", &n);
    scanf("%d", &m);

    if (n < m) {
        x = &b[0]; y = &a[0];
    }

    for (int i = 0; i < n; i++)
        scanf("%d", x + i);

    for (int i = 0; i < m; i++)
        scanf("%d", y + i);

    if (n < m) {
        int temp = n;
        n = m;
        m = temp;
    }

    sort(a, a + n);
    sort(b, b + m);

    unsigned int sol = -1;

    for (int o = 0; o <= n - m; o++) {
        int mr = 0;
        int i;
        for (i = 0; i < m; i++) {
            int r = abs(b[i], a[i + o]);
            if (r > sol) break;
            if (r > mr)  mr = r;
        }
        if (i == m) sol = mr;
    }

    printf("%d\n", sol);

    return 0;
}