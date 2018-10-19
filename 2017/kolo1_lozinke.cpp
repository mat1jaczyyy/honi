#include <cstdio>
#include <vector>
using namespace std;

int subvector(vector<char> haystack, vector<char> needle) {
	int pos = 0;
	for (int i = 0; i < haystack.size(); i++) {
		if (haystack[i] == needle[pos]) {
			pos++;
			if (pos == needle.size()) {
				return 1;
			}
		} else {
			pos = 0;
		}
	}
	return 0;
}

int main() {
	int n;
	scanf("%d", &n);
	
	vector<char> a[n];
	int i = 0; char t;
	int c = 0;
	scanf("%c");
	
	while (i < n) {
		scanf("%c", &t);
		if (t == '\n') {
			for (int j = 0; j < i; j++) {
				c += subvector(a[i], a[j]);
				c += subvector(a[j], a[i]);
			}
			i++;
		} else {
			a[i].push_back(t);
		}
	}
	
	printf("%d\n", c);
	
	return 0;
}
