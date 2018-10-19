n, m, k = [int(i) for i in input().split()]

r = [1] * n
s = [1] * m

for i in range(k):
	x = input().split()
	if x[0] == "R":
		r[int(x[1]) - 1] *= int(x[2])
	if x[0] == "S":
		s[int(x[1]) - 1] *= int(x[2])
	

c = 0
for i in range(n):
	for j in range(m):
		c += (i * m + j + 1) * r[i] * s[j]

print(c)