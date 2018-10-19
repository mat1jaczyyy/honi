#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	
	int a[n][m];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	
	int q;
	scanf("%d", &q);
	
	for (int _ = 0; _ < q; _++) {
		int b;
		vector<int> s;
		
		for (int i = 0; i < n; i++) {
			s.push_back(i);
		}
		
		
		for (int j = 0; j < m; j++) {
			vector<int> t;
			scanf("%d", &b);
			
			if (b > 0) {
				for (int i = 0; i < s.size(); i++) {
					if (a[s[i]][j] == b) {
						t.push_back(s[i]);
					}
				}
				s = t;
			}
		}
		
		printf("%d\n", s.size());
	}
	
	return 0;
}
