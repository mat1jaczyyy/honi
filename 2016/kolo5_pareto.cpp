#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	
	int b[n];
	long long int sum = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d", &b[i]);
		sum += b[i];
	}
	
	sort(b, b+n);
	
	long long int right = sum - b[0];
	
	double A, B, diff;
	double best_A = 1;
	double best_B = 0;
	double best_diff = -1;
	for (int i = 1; i < n; i++) {
		A = (double)(n - i) / (double)n;
		/*if ((double)1 - A < best_diff) {
			printf("Better than best_diff %f\n", (double)1 - A);
			break;
		}*/
		B = (double)((long double)right / (long double)sum);
		diff = B - A;
		if (diff > best_diff) {
			best_A = A;
			best_B = B;
			best_diff = diff;
		}
		right += -b[i];
	} 
	
	printf("%f\n%f\n", best_A * 100, best_B * 100);
	
	return 0;
}
