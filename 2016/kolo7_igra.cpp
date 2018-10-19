#include <cstdio>
#include <vector>
using namespace std;

int x;

int main() {
	int n;
	scanf("%d", &n);
	
	int m[n];
	int c[3]; c[0] = 0; c[1] = 0; c[2] = 0;
	
	for (int i = 0; i < n; i++) {
		scanf(" %c", &x);
		m[i] = x - 97;
		c[m[i]]++;
	}
	
	for (int i = 0; i < n; i++) {
		scanf(" %c", &x);
		
		if (x == 97) {
			if (c[1] > 0) {
				printf("b"); c[1]--;
			} else {
				printf("c"); c[2]--;
			}
		} else if (x == 98) {
			if (c[0] > 0) {
				printf("a"); c[0]--;
			} else {
				printf("c"); c[2]--;
			}
		} else {
			if (c[2] > 0) {
				printf("a"); c[0]--;
			} else {
				printf("b"); c[1]--;
			}
		}
	}
	
	printf("\n");
	return 0;
}
