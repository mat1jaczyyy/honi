n, m, k, x = [int(i) for i in input().split()]
r = list(input())
t = [''.join(sorted(input())) for i in range(m)]
x += -1

d = range(26)
y = []
while x:
	y += [d[x % k]]
	x = x // k
y += [0] * (m - len(y))
y.reverse()

i = 0
while '#' in r:
	r[r.index('#')] = t[i][y[i]]
	i += 1

print("".join(r))