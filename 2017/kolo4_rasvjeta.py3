import math

n = int(input())
m = int(input())
k = int(input())
l = [0] * (n+1)
l[-1] = -1

for i in range(m):
	x = int(input()) - 1
	for j in range(max(0, x - k), min(n, x + k + 1)):
		l[j] = 1

k = 2*k + 1
s = 0
c = 0
prev = -1
for i in range(n+1):
	if prev != l[i]:
		if prev == 0:
			s += math.ceil(c / k)
		c = 1
		prev = l[i]
	else:
		c += 1

print(s)