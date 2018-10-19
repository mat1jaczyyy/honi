n = int(input())

p = [None] * n
k = [None] * n
m = [None] * n
e = [None] * n
s = 0

for i in range(n):
	p[i] = input()
	k[i], m[i] = [int(j) for j in input().split()]
	
	if m[i] < k[i]:
		e[i] = 0
	else:
		e[i] = int((m[i] - k[i]) / (k[i] - 2)) + 1

	s += e[i]

print(s)
print(p[e.index(max(e))])