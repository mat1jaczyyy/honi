n, k = [int(i) for i in input().split()]
h, g, p = [], [], []
for i in range(n):
	_h, _g = [int(i) for i in input().split()]
	h.append(_h)
	g.append(_g)
	p.append([_g])

rj = 0
if p[-1][0] >= k:
	rj = 1

for i in range(n, -1, -1):
	for j in range(i + 1, n):
		if h[j] >= h[i]:
			for c in p[j]:
				p[i].append(g[i] + c)
				if p[i][-1] >= k:
					rj += 1

print(rj)