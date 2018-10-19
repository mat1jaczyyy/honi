import sys

def split(n, m):
	for i in range(0, len(n), m):
		yield n[i:i+m]

s = input()
l = len(s)

if all(i == s[0] for i in s):
	print(s[0])
	sys.exit()

for i in range(2, l // 2 + 1):
	if l % i == 0:
		k = [sorted(j) for j in split(s, i)]
		if all(i == k[0] for i in k):
			print(s[:i])
			sys.exit()

print(-1)