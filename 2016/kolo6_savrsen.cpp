#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

int main() {
	int a, b;
	scanf("%d %d", &a, &b);
	
	int sol = 0;
	for (int i = a; i <= b; i++) {
		int score = 1;
		
		double rsqrt = sqrt(i);
		int c = ceil(rsqrt);
		for (int j = 2; j < c; j++) {
			if (i % j == 0) {
				score += j;
				score += (i / j);
			}
		}
		if (c*c == i) {
			score += c;
		}
		
		sol += abs(i - score);
	}
	
	printf("%d\n", sol);
}
