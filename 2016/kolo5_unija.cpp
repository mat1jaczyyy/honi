#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	
	int x[n], y[n];
	int max_y = -1;
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &x[i], &y[i]);
		x[i] /= 2; y[i] /= 2;
		if (y[i] > max_y) {
			max_y = y[i];
		}
	}
	
	int m[max_y]; std::fill_n(m, max_y, 0);
	unsigned long long sum = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < y[i]; j++) {
			if (x[i] > m[j]) {
				sum += x[i] - m[j];
				m[j] = x[i];
			}
		}
	}
	
	printf("%lld\n", sum * 4);
	
	return 0;
}
