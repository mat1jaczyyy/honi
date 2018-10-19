from collections import deque
from sys import stdin

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def bfs(a, b):
	global n, g
	
	w = [1000000005] * n
	w[a] = 0
	
	q = deque([a])
	rj = []	

	while len(q) > 0:
		c = q.popleft()
		for i in g[c]:
			if w[i] > g[c][i]:
				w[i] = g[c][i]
				
				if i == b:
					rj.append(w[i])
					
				q.append(i)
	return w[b]

n, m, q = [int(i) for i in stdin.readline().split()]

g = [{} for i in range(n)]
for i in range(n):
	for j in range(n):
		k = m - gcd(i + 1, j + 1) + 1
		if k > 0:
			g[i][j] = k	

for _ in range(q):
	a, b = [int(i) for i in stdin.readline().split()]
	print(bfs(a - 1, b - 1))
