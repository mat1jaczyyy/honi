import itertools

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

y = []
for i in itertools.combinations(range(n), k):
	z = [0] * k
	for j in range(k):
		z[j] = a[i[j]]
	y.append(z)

print(sum([max(i) for i in y]))