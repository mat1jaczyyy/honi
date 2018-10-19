r, s = [int(i) for i in input().split()]
a = []
v = []
e = []

for _ in range(r):
	a.append(list(input()))
	for __ in range(s):
		v.append(a[_][__])
		e.append([])

p = e.copy()
x = a[-1].index("M")

for i in range(r - 1, 0, -1):
	for j in range(max(0, x - r + i), min(s, x + r - i)):
		if a[i][j] != "*" and i > 0:
			e[i*s+j] = []
			for k in range(max(0, j - 1), min(s, j + 2)):
				if a[i-1][k] != "*":
					e[i*s+j].append((i-1)*s+k)

from collections import deque

q = deque([(r - 1) * s + x])
p[(r - 1) * s + x].append([])
d = [False] * (r * s)
z = []

while len(q):
	c = q.popleft()
	if not d[c]:
		for n in e[c]:
			for i in p[c]:
				p[n].append(i.copy())
				if v[c] == "(" or v[c] == ")":
					p[n][-1].append(v[c])
			if n >= s:
				q.append(n)
		d[c] = True

y = []
l = 2
for i in range(len(v)):
	for j in p[i]:
		if v[i] == "(" or v[i] == ")":
			j.append(v[i])
		if len(j) >= l and len(j) % 2 == 0:
			depth = 0
			for k in j:
				depth += (1 if k == "(" else -1)
				if depth < 0:
					break
			if depth == 0:
				if len(j) > l:
					y = []
					l = len(j)
				if len(j) == l:
					y.append(''.join(j))

y.sort()
print(l)
print(y[0])