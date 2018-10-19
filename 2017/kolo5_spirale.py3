class Spirala:
	def __init__(self, i):
		self.x = i[0] + n
		self.y = i[1] + m
		self.t = i[2]
	
	def update(self):
		global g, c
		
		if not g[self.x][self.y]:
			g[self.x][self.y] = p
			if n < self.x <= 2*n and m < self.y <= 2*m:
				c += 1
		
		if d == 0:
			self.x += -1
		elif d == 1 + (self.t*2):
			self.y += 1
		elif d == 2:
			self.x += 1
		elif d == 3 - (self.t*2):
			self.y += -1

n, m, k = [int(i) for i in input().split()]
s = [Spirala([int(i) for i in input().split()]) for j in range(k)]
g = [[0] * (3*n + 2) for i in range(3*m + 2)]

c = 0
z = 1
e = 2
d = 0
p = 1
while c < n * m:
	for i in s:
		i.update()
	
	e += -1
	if not e:
		z += 1
		e = 2*z
	
	if not e % z:
		d = (d + 1)%4
	
	p += 1

print('\n'.join([' '.join([str(g[i][j]) for j in range(m + 1, 2*m + 1)]) for i in range(n + 1, 2*n + 1)]))
