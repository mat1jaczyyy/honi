def process(i):
	global c, o, h
	p = 1
	
	if c == 1:
		c = 0
	elif len(z[i]) - o[i]:
		p = process(z[i][o[i]])
		if p == 2:
			o[i] += 1
			c += -1
	
	h[i] += p
	return p + 1

n = int(input())
z = [[] for i in range(n)]

_ = [int(i) for i in input().split()]
for i in range(n - 1):
	z[_[i] - 1].append(i + 1)

c = n
o = [0] * n
h = [0] * n

while c:
	process(0)

print(' '.join([str(i) for i in h]))
