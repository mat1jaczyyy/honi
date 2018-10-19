max = 0
n, c = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]

for k in range(n):
	s = 0
	l = 0
	for i in range(k, n):
		s += w[i]
		if s > c:
			break
		l += 1
	if l > max:
		max = l

print(max)