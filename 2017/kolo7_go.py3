from itertools import permutations

n, k, m = [int(i) for i in input().split()]
p = []

for _ in range(m):
	p.append([int(i) for i in input().split()])

best = 0
for i in permutations(p, len(p)):
	sol = 0
	time = 0
	pos = k
	for j in i:
		time += abs(pos - j[0])
		pos = j[0]
		if time < j[2]:
			sol += j[1]
	if sol > best:
		best = sol
print(best)
