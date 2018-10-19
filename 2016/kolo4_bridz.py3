n = int(input())
k = [input() for i in range(n)]

m = {"A": 4, "K": 3, "Q": 2, "J": 1, "X": 0}
s = 0

for i in k:
	for c in i:
		s += m[c]

print(s)