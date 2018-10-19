#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	
	int a[n];
	for (int _ = 0; _ < n; _++) {
		scanf("%d", &a[_]);
	}
	
	sort(a, a + n);
	for (int _ = n - 1; _ >= 0; _--) {
		if (a[_] < n - _) {
			printf("%d\n", n - _ - 1);
			return 0;
		}
	}
	
	printf("%d\n", n);
	return 0;
}

// 1 1 1 4 8
// 5 4 3 2 1
