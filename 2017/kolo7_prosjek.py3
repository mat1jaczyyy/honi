n = int(input())
x = [float(input()) for i in range(n)]

x.sort()

for i in range(1, n):
	x[i] = (x[i] + x[i - 1]) / 2

print(x[-1])
