#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

int k, j, r, a, b;

int main() {
	int n;
	scanf("%d", &n);
	
	for (int i = 1; i <= sqrt(n); i++) {
		if (n % i == 0) {
			k = i;
			j = (int)(n / k);
			if (j % 2 == 1) {
				r = (int)(j / 2);
				a = k - r;
				b = k + r;
				if (a <= 0)
					a = abs(a) + 1;
				printf("%d %d\n", a, b);
			}
			if (k > 1 && k % 2 == 1 && k != j) {
				r = (int)(k / 2);
				a = j - r;
				b = j + r;
				if (a <= 0)
					a = abs(a) + 1;
				printf("%d %d\n", a, b);
			}
		}
	}
	
	return 0;
}
