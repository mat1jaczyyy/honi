global n, m, w
n, m = [int(i) for i in input().split()]

w = [input() for i in range(n)]

nodes = n * m
start = 0
end = n * m - 1
edge = []
for i in range(n):
	for k in range(m):
		edge += [[]]
		if k != m - 1:
			edge[(i * m) + k] += [[(i * m) + k + 1, ord(w[i][k+1])]]
		if i != n - 1:
			edge[(i * m) + k] += [[((i+1) * m) + k, ord(w[i+1][k])]]

def bfs(nodes, edge, start, end):
	from collections import deque
	
	distance = [-1] * nodes
	distance[start] = 0
	
	path = [[]] * nodes
	path[start] = [start]
	
	q = deque([start])
	
	while len(q) > 0:
		current = q.popleft()
		for node in edge[current]:
			if distance[current] + node[1] < distance[node[0]] or distance[node[0]] == -1:
				distance[node[0]] = distance[current] + node[1]
				path[node[0]] = path[current] + [node[0]]
				q.append(node[0])
	
	return path[node[0]]

print(''.join([w[i // m][i % m] for i in bfs(nodes, edge, start, end)]))