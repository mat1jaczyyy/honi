#include <cstdio>
using namespace std;

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	
	char a[n][m];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%c", &a[i][j]);
			if (a[i][j] == '\n') {
				j--;
			}
		}
	}
	
	int c[5];
	for (int i = 0; i < 5; i++) {
		c[i] = 0;
	}
	
	/*
		[][]
		[][]
	*/
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < m - 1; j++) {
			if (a[i][j] != '.') {
				c[0] += int(a[i + 1][j] == a[i][j] && a[i][j + 1] == a[i][j] && a[i + 1][j + 1] == a[i][j]);
			}
		}
	}
	
	/*
		[][][][]
	*/
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m - 3; j++) {
			if (a[i][j] != '.') {
				c[1] += int(a[i][j + 1] == a[i][j] && a[i][j + 2] == a[i][j] && a[i][j + 3] == a[i][j]);
			}
		}
	}
	
	/*
		[]
		[]
		[]
		[]
	*/
	for (int i = 0; i < n - 3; i++) {
		for (int j = 0; j < m; j++) {
			if (a[i][j] != '.') {
				c[1] += int(a[i + 1][j] == a[i][j] && a[i + 2][j] == a[i][j] && a[i + 3][j] == a[i][j]);
			}
		}
	}
	
	/*
		  [][]
		[][]
	*/
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < m - 2; j++) {
			if (a[i][j] != '.') {
				c[2] += int(a[i][j + 1] == a[i][j] && a[i - 1][j + 1] == a[i][j] && a[i - 1][j + 2] == a[i][j]);
			}
		}
	}
	
	/*
		[]
		[][]
		  []
	*/
	for (int i = 0; i < n - 2; i++) {
		for (int j = 0; j < m - 1; j++) {
			if (a[i][j] != '.') {
				c[2] += int(a[i + 1][j] == a[i][j] && a[i + 1][j + 1] == a[i][j] && a[i + 2][j + 1] == a[i][j]);
			}
		}
	}
	
	/*
		[][]
		  [][]
	*/
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < m - 2; j++) {
			if (a[i][j] != '.') {
				c[3] += int(a[i][j + 1] == a[i][j] && a[i + 1][j + 1] == a[i][j] && a[i + 1][j + 2] == a[i][j]);
			}
		}
	}
	
	/*
		  []
		[][]
		[]
	*/
	for (int i = 2; i < n; i++) {
		for (int j = 0; j < m - 1; j++) {
			if (a[i][j] != '.') {
				c[3] += int(a[i - 1][j] == a[i][j] && a[i - 1][j + 1] == a[i][j] && a[i - 2][j + 1] == a[i][j]);
			}
		}
	}
	
	/*
		  []
		[][][]
	*/
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < m - 2; j++) {
			if (a[i][j] != '.') {
				c[4] += int(a[i][j + 1] == a[i][j] && a[i - 1][j + 1] == a[i][j] && a[i][j + 2] == a[i][j]);
			}
		}
	}
	
	/*
		[]
		[][]
		[]
	*/
	for (int i = 0; i < n - 2; i++) {
		for (int j = 0; j < m - 1; j++) {
			if (a[i][j] != '.') {
				c[4] += int(a[i + 1][j] == a[i][j] && a[i + 1][j + 1] == a[i][j] && a[i + 2][j] == a[i][j]);
			}
		}
	}
	
	/*
		[][][]
		  []
	*/
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < m - 2; j++) {
			if (a[i][j] != '.') {
				c[4] += int(a[i][j + 1] == a[i][j] && a[i + 1][j + 1] == a[i][j] && a[i][j + 2] == a[i][j]);
			}
		}
	}
	
	/*
		  []
		[][]
		  []
	*/
	for (int i = 0; i < n - 2; i++) {
		for (int j = 1; j < m; j++) {
			if (a[i][j] != '.') {
				c[4] += int(a[i + 1][j] == a[i][j] && a[i + 1][j - 1] == a[i][j] && a[i + 2][j] == a[i][j]);
			}
		}
	}
	
	for (int i = 0; i < 5; i++) {
		printf("%d\n", c[i]);
	}
	return 0;
}
