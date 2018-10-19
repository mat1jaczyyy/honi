import sys

n = int(sys.stdin.readline())
x = int(sys.stdin.readline())

sol = 0
for _ in range(n):
	p = [int(i) for i in sys.stdin.readline().split()]
	if abs(p[0] - p[1]) > x:
		sol += int(sys.stdin.readline())
	else:
		sol += max(p)

sys.stdout.write(str(sol) + "\n")