n = int(input())
c = [int(input()) for i in range(n)]

c.sort()

import itertools

x = 0

def powerset(arr):
    s = list(arr)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1, len(s)+1))

z = []
last = -1
for i in c:
	if last == i:
		last = -1
		del z[-1]
		x += i
	else:
		z += [i]
		last = i

c = z

def list_subtract(a, b):
	hfewu = a
	for i in range(len(b)):
		if list(reversed(b))[i] in hfewu:
			del hfewu[hfewu.index(list(reversed(b))[i])]
	return hfewu

def getmax(asd):
	best = [[-1,-1],[-1,-1]]
	for gospa in asd:
		if sum(gospa[0]) > sum(best[0]):
			best = gospa
	return best

sums = [[-1,-1]]
while sums != []:
	sums = []
	for j in powerset(c):
		isus = []
		isus += c
		for i in powerset(list_subtract(isus, list(j))):
			if sum(i) == sum(j):
				sums += [[i, j]]
	if sums != []:
		best = getmax(sums)
		x += sum(best[0])
		deletion = list(best[0]) + list(best[1])
		deletion.sort()
		z = c
		for k in reversed(deletion):
			del z[z.index(k)]
		c = z

print(x + sum(c))