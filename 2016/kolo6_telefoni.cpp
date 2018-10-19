#include <cstdio>
using namespace std;

int main() {
	int n, d;
	scanf("%d %d", &n, &d);
	
	int c = 0;
	int sol = 0;
	for (int _ = 0; _ < n; _++) {
		int x;
		scanf("%d", &x);
		if (x == 1 && c > 0) {
			sol += c / d;
			c = 0;
		} else if (x == 0) {
			c++;
		}
	}
	
	printf("%d\n", sol);
	
	return 0;
}
