import sys

n, q = [int(i) for i in sys.stdin.readline().split()]

a = [int(i) for i in sys.stdin.readline().split()]

for _ in range(q):
	l, r = [int(i) for i in sys.stdin.readline().split()]
	c = [0] * n
	w = 0
	for i in a[l-1:r]:
		c[i] += 1
		if c[i] == 2:
			w += 1
		if c[i] == 3:
			w += -1
	sys.stdout.write(str(w) + "\n")
		