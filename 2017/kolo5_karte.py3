n, k = [int(i) for i in input().split()]
a = [int(input()) for i in range(n)]

from itertools import permutations

for x in permutations(a):
	c = k
	l = 0
	for i in range(n):
		if l != x[i]:
			c += -1
			l += 1
	
	if not c:
		print(' '.join([str(i) for i in x]))
		break
