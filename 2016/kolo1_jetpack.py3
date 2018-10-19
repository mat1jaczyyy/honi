global n
n = int(input())
m = [input() for i in range(10)]

class Coord():
	def __init__(self, x, y):
		self.x, self.y = x, y
	def __str__(self):
		return "Coord(" + str(self.x) + ", " + str(self.y) + ")"
	def __repr__(self):
		return self.__str__()
	def __eq__(self, b):
		return ((self.x == b.x) and (self.y == b.y))

global edge
edge = [[[] for k in range(n)] for i in range(10)]
for x in range(10):
	for y in range(n - 1):
		if (x == 0 or x == 9) and m[x][y+1] == ".":
			edge[x][y] += [Coord(x, y+1)]
		if x != 0:
			if m[x-1][y+1] == ".":
				edge[x][y] += [Coord(x-1, y+1)]
		if x != 9:
			if m[x+1][y+1] == ".":
				edge[x][y] += [Coord(x+1, y+1)]

from collections import deque
	
def bfs():
	start = Coord(9, 0)
	
	distance = [[-1 for k in range(n)] for i in range(10)]
	distance[start.x][start.y] = 0
	
	path = [[[[]] for k in range(n)] for i in range(10)]
	path[start.x][start.y] = [start]
	
	q = deque([start])
	
	while len(q) > 0:
		current = q.popleft()
		for node in edge[current.x][current.y]:
			if distance[node.x][node.y] < 0:
				distance[node.x][node.y] = distance[current.x][current.y] + 1
				path[node.x][node.y] = path[current.x][current.y] + [node]
				
				if node.y == n - 1:
					return path[node.x][node.y]
				
				q.append(node)

play = bfs()

history = []
state = False
out = []
c = 0

for k in play:
	if len(history) > 0:
		if state == False:
			if history[-1] > k.x:
				state = True
				out += [str(k.y - 1) + " "]
				c += 1
		else:
			if history[-1] < k.x:
				state = False
				out[-1] += str(c)
				c = 0
			else:
				c += 1
	history += [k.x]

if out[-1][-1] == " ":
	out[-1] += str(c)

print(len(out))

if len(out) > 0:
	for o in out:
		print(o)