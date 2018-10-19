r, s, k = [int(i) for i in input().split()]
m = [input() for i in range(r)]

q = r - k + 1
p = s - k + 1
x = 0
y = 0
z = 0

for i in range(q):
	for j in range(p):
		c = 0
		for o in range(i + 1, i + k - 1):
			c += m[o][j + 1 : j + k - 1].count("*")
		if c > z:
			x = i
			y = j
			z = c

print(z)

for i in range(x):
	print(m[i])

print(m[x][: y] + "+" + ("-" * (k - 2)) + "+" + m[x][y + k :])

for i in range(x + 1, x + k - 1):
	print(m[i][: y] + "|" + m[i][y + 1 : y + k - 1] + "|" + m[i][y + k :])

print(m[x + k - 1][: y] + "+" + ("-" * (k - 2)) + "+" + m[x + k - 1][y + k :])

for i in range(x + k, r):
	print(m[i])