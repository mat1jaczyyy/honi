from itertools import combinations

def win(a, x):
	c = [0] * m
	for i in range(n):
		y = a[i][0]
		j = 1
		while y in x:
			y = a[i][j]
			j += 1
		c[y] += 1
	return c.index(max(c))

n, m, k = [int(i) for i in input().split()]
k += -1
a = [[int(j) - 1 for j in input().split()] for i in range(n)]
x = []

w = win(a, x)
print(w + 1)

b = 0
for i in range(m):
	for j in range(n):
		if a[j][i] == k:
			z = i
			b = 1
			break
	if b > 0:
		break

t = combinations(range(15), r = z)

while w != k:
	try:
		x = next(t)
	except:
		z += 1
		t = combinations(range(15), r = z)
	w = win(a, x)

print(z)