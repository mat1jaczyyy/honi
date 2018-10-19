#include <cstdio>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);

	int c[10];
	for (int i = 0; i < 10; i++) {
		c[i] = 4;
	}
	c[8] = 16;

	int x, s = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d", &x);
		s += x;
		c[x - 2]--;
	}

	s = 21 - s;

	if (s > 10) {
		printf("VUCI\n");
		return 0;
	}

	int a = 0;
	int b = 0;
	for (int i = 0; i < 10; i++) {
		if (i + 2 <= s) {
			a += c[i];
		} else {
			b += c[i];
		}
	}

	if (b >= a) {
		printf("DOSTA\n");
	} else {
		printf("VUCI\n");
	}

	return 0;
}
