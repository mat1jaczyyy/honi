#include <cstdio>
#include <math.h>
#include <set>
using namespace std;

int a[1048577], c[1048577], s[1048577];

int bitf(int num) {
	int i = -1;
	for (int t = 1; t <= num; t *= 2) {
		i++;
	}
	return i;
}

int main() {
	int n;
	scanf("%d", &n);
	int m = pow(2, n);

	set<int> e;
	e.insert(0);
	for (int _ = 0; _ < m; _++) {
		scanf("%d", &a[_]);
		c[a[_]]++;
		e.insert(a[_]);
	}
	
	int prev = 0;
	for (auto i : e) {
		s[i] = c[i] + s[prev];
		prev = i;
	}
	
	for (int _ = 0; _ < m - 1; _++) {
		printf("%d ", n - bitf(s[a[_]]));
	}
	printf("%d\n", n - bitf(s[a[m - 1]]));
	
	return 0;
}



// 11 -> 00000000 00000000 00000000 00001011
