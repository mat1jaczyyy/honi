import sys

k = int(sys.stdin.readline())
d = int(sys.stdin.readline())
o = int(sys.stdin.readline())

for i in range(1, 10001):
	if (i * k) % d == o:
		sys.stdout.write(str(i) + "\n")
		sys.exit()

sys.stdout.write("-1\n")